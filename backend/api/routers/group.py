from fastapi import APIRouter, Depends, HTTPException, status
from random import shuffle

from .depends import check_course_id, check_group_id, check_user_id
from crud.group import GroupCrudManager
from crud.selected_course import SelectedCourseCrudManager
from schemas import group as GroupSchema
from schemas import selected_course as SelectedCourseSchema

not_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Group does not exist"
)

GroupCrud = GroupCrudManager()
SelectedCourseCrud = SelectedCourseCrudManager()
router = APIRouter(
    tags=["Group"],
    prefix="/api"
)


@router.post(
    "/grouping/auto",
    response_model=list[GroupSchema.GroupAutoCreateResponse],
    status_code=status.HTTP_201_CREATED
)
async def auto_grouping(
    grouping_method: GroupSchema.GroupingMethod,
    number_depend_on_grouping_method: int,
    distributing_method: GroupSchema.DistributingMethod,
    naming_rule: GroupSchema.NamingRule,
    course_id: str = Depends(check_course_id)
):
    """
    Auto grouping.
    """
    groups = []
    members = await SelectedCourseCrud.get_by_course_id(course_id)
    members = [{"uid": member["uid"], "name": member["name"]} for member in members if member["role"] == "student"]
    
    # Fake data from A to L
    members = [{'uid': 'K', 'name': 'K-name'}, {'uid': 'D', 'name': 'D-name'}, {'uid': 'E', 'name': 'E-name'}, {'uid': 'C', 'name': 'C-name'}, {'uid': 'B', 'name': 'B-name'}, {'uid': 'L', 'name': 'L-name'}, {'uid': 'G', 'name': 'G-name'}, {'uid': 'I', 'name': 'I-name'}, {'uid': 'J', 'name': 'J-name'}, {'uid': 'H', 'name': 'H-name'}, {'uid': 'F', 'name': 'F-name'}, {'uid': 'A', 'name': 'A-name'}, {'uid': 'M', 'name': 'M-name'}, {'uid': 'N', 'name': 'N-name'}]
    
    # Distributing method: random or by first name
    if distributing_method == GroupSchema.DistributingMethod.random:
        shuffle(members)
    elif distributing_method == GroupSchema.DistributingMethod.first_name:
        members = sorted(members, key=lambda member: member["name"])

    # Grouping method: numbers of groups or numbers of members
    if grouping_method == GroupSchema.GroupingMethod.numbers_of_groups:
        group_num = number_depend_on_grouping_method
        members_per_group = len(members) // group_num
        remainder = len(members) % group_num
        for i in range(group_num):
            newGroup = {
                "number_of_members": members_per_group + 1 if remainder > 0 else members_per_group,
                "members": [],
            }
            newGroup["members"] = [members.pop(0) for _ in range(newGroup["number_of_members"])]
            remainder -= 1
            groups.append(newGroup)
            
    elif grouping_method == GroupSchema.GroupingMethod.numbers_of_members:
        members_per_group = number_depend_on_grouping_method
        group_number = len(members) // members_per_group + 1
        for i in range(group_number):
            newGroup = {
                "number_of_members": len(members[i * members_per_group: (i + 1) * members_per_group]),
                "members": members[i * members_per_group: (i + 1) * members_per_group]
            }
            groups.append(newGroup)
    
    # Update database
    group_name = 65 if naming_rule == GroupSchema.NamingRule.alphabet else 1
    for group_info in groups:
        name = chr(group_name) if naming_rule == GroupSchema.NamingRule.alphabet else str(group_name)
        group_schema = GroupSchema.GroupCreate(name=name, number_of_members=group_info["number_of_members"])
        group = await GroupCrud.create(course_id, group_schema)
        group_info.update({
            "id": group.id,
            "name": name
        })
        
        for member in group_info["members"]:
            await SelectedCourseCrud.update(member["uid"], course_id, group_info["id"])
        
        group_name += 1
                
    return groups


@router.post(
    "/grouping/student",
    response_model=list[GroupSchema.GroupAutoCreateResponse],
    status_code=status.HTTP_201_CREATED
)
async def student_grouping(
    grouping_method: GroupSchema.GroupingMethod,
    number_depend_on_grouping_method: int,
    naming_rule: GroupSchema.NamingRule,
    create_deadline: str,
    course_id: str = Depends(check_course_id)
):
    """
    Students group by themselves.
    """
    groups = []
    members = await SelectedCourseCrud.get_by_course_id(course_id)
    members = [member for member in members if member["role"] == "student"]
    
    # Fake data from A to L
    members = [{'uid': 'K', 'name': 'K-name'}, {'uid': 'D', 'name': 'D-name'}, {'uid': 'E', 'name': 'E-name'}, {'uid': 'C', 'name': 'C-name'}, {'uid': 'B', 'name': 'B-name'}, {'uid': 'L', 'name': 'L-name'}, {'uid': 'G', 'name': 'G-name'}, {'uid': 'I', 'name': 'I-name'}, {'uid': 'J', 'name': 'J-name'}, {'uid': 'H', 'name': 'H-name'}, {'uid': 'F', 'name': 'F-name'}, {'uid': 'A', 'name': 'A-name'}, {'uid': 'M', 'name': 'M-name'}, {'uid': 'N', 'name': 'N-name'}]

    # Grouping method: numbers of groups or numbers of members
    if grouping_method == GroupSchema.GroupingMethod.numbers_of_groups:
        group_num = number_depend_on_grouping_method
        members_per_group = len(members) // group_num
        remainder = len(members) % group_num
        for i in range(group_num):
            newGroup = {
                "number_of_members": members_per_group + 1 if remainder > 0 else members_per_group,
                "members": []
            }
            remainder -= 1
            groups.append(newGroup)
            
    elif grouping_method == GroupSchema.GroupingMethod.numbers_of_members:
        members_per_group = number_depend_on_grouping_method
        group_number = len(members) // members_per_group + 1
        for i in range(group_number):
            newGroup = {
                "number_of_members": len(members[i * members_per_group: (i + 1) * members_per_group]),
                "members": []
            }
            groups.append(newGroup)
    
    # Naming rule: alphabet or number AND create groups
    group_name = 65 if naming_rule == GroupSchema.NamingRule.alphabet else 1
    for group_info in groups:
        name = chr(group_name) if naming_rule == GroupSchema.NamingRule.alphabet else str(group_name)
        group_schema = GroupSchema.GroupCreate(name=name, number_of_members=group_info["number_of_members"])
        group = await GroupCrud.create(course_id=course_id, newGroup=group_schema, create_deadline=create_deadline)
        group_info.update({
            "id": group.id,
            "name": name
        })
        group_name += 1
        
    return groups
       

@router.post(
    "/grouping/manual", 
    status_code=status.HTTP_204_NO_CONTENT
)
async def manual_grouping(
    newGroup: GroupSchema.GroupManualCreate,
    course_id: str = Depends(check_course_id)
):
    """
    Manual grouping with the following information:
    - **name**
    - **members** (list)
        - **uid**
        - **name**
    """
    await GroupCrud.manual_create(course_id, newGroup)

    return


@router.get(
    "/groups",
    status_code=status.HTTP_200_OK,
    deprecated=True
)
async def get_all_groups():
    """ 
    Get all groups.
    """
    groups = await GroupCrud.get_all()
    if groups:
        return groups
    
    raise not_found


@router.get(
    "/group/info/{course_id}", 
    response_model=list[GroupSchema.GroupReadByCourseID],
    status_code=status.HTTP_200_OK
)
async def get_all_groups_in_one_coure(
    course_id: str = Depends(check_course_id)
):
    group = await GroupCrud.get_by_course_id(course_id)
    if group:
        return group
    
    raise not_found

    
@router.put(
    "/group/join",
    status_code=status.HTTP_204_NO_CONTENT
)
async def join_group(
    uid: str = Depends(check_user_id),
    course_id: str = Depends(check_course_id),
    group_id: int = Depends(check_group_id)
):
    """ 
    Add user into the group.
    """
    await GroupCrud.join(uid, course_id, group_id)

    return 


@router.put(
    "/group/exit",
    status_code=status.HTTP_204_NO_CONTENT
)
async def exit_group(
    uid: str = Depends(check_user_id),
    course_id: str = Depends(check_course_id)
):
    """ 
    Exit group.
    """
    await GroupCrud.exit(uid, course_id)

    return 


@router.put(
    "/group/{group_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_group_info(
    updateGroup: GroupSchema.GroupUpdate,
    group_id: int = Depends(check_group_id)
):
    """ 
    Update the group information:
    - **name**
    """
    await GroupCrud.update(group_id, updateGroup)

    return 


@router.delete(
    "/group/{group_id}",
    status_code=status.HTTP_204_NO_CONTENT 
)
async def delete_group(group_id: int = Depends(check_group_id)):
    """ 
    Delete the group.
    """
    await GroupCrud.delete(group_id)
    
    return 
