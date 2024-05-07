from fastapi import APIRouter, Depends, HTTPException, status
from random import shuffle

from .depends import check_course_id, check_group_id
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
    "/group", 
    status_code=status.HTTP_204_NO_CONTENT
)
async def create_one_group(
    newGroup: GroupSchema.GroupCreate,
    course_id: str = Depends(check_course_id)
):
    """
    Create a group with the following information:
    - **name**
    """
    await GroupCrud.create(course_id, newGroup)

    return


@router.post(
    "/grouping/auto", 
    status_code=status.HTTP_200_OK
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
    members = await SelectedCourseCrud.get_by_course_id(course_id)
    members = [{"uid": member["uid"], "name": member["name"]} for member in members if member["role"] == "student"]
    group_dict = {}

    # Fake data from A to L
    # members = [{'uid': 'K', 'name': 'K-name'}, {'uid': 'D', 'name': 'D-name'}, {'uid': 'E', 'name': 'E-name'}, {'uid': 'C', 'name': 'C-name'}, {'uid': 'B', 'name': 'B-name'}, {'uid': 'L', 'name': 'L-name'}, {'uid': 'G', 'name': 'G-name'}, {'uid': 'I', 'name': 'I-name'}, {'uid': 'J', 'name': 'J-name'}, {'uid': 'H', 'name': 'H-name'}, {'uid': 'F', 'name': 'F-name'}, {'uid': 'A', 'name': 'A-name'}, {'uid': 'M', 'name': 'M-name'}, {'uid': 'N', 'name': 'N-name'}]
    
    # Distributing method: random or by first name
    if distributing_method == GroupSchema.DistributingMethod.random:
        shuffle(members)
    elif distributing_method == GroupSchema.DistributingMethod.first_name:
        members = sorted(members, key=lambda member: member["name"])

    # Grouping method: numbers of groups or numbers of members
    if grouping_method == GroupSchema.GroupingMethod.numbers_of_groups:
        group_num = number_depend_on_grouping_method
        members_per_group, remainder = len(members) // group_num, len(members) % group_num
        for i in range(group_num):
            _members_per_group = members_per_group + 1 if remainder > 0 else members_per_group
            group_dict[i] = []
            for _ in range(_members_per_group):
                group_dict[i].append(members.pop(0))

            remainder = remainder - 1 if remainder > 0 else 0
    elif grouping_method == GroupSchema.GroupingMethod.numbers_of_members:
        members_per_group = number_depend_on_grouping_method
        group_number = len(members) // number_depend_on_grouping_method
        for i in range(group_number):
            group_dict[i] = members[i * members_per_group: (i + 1) * members_per_group]
        group_dict[group_number] = members[group_number * members_per_group:]
    
    # Naming rule: alphabet or number
    group_id_list = []
    group_name_list = []
    group_name = 65 if naming_rule == GroupSchema.NamingRule.alphabet else 1
    for i in range(len(group_dict)):
        name = chr(group_name) if naming_rule == GroupSchema.NamingRule.alphabet else str(group_name)
        group = await GroupCrud.create(course_id, GroupSchema.GroupCreate(name=name))
        group_id_list.append(group.id)
        group_name_list.append(name)
        group_name += 1
    
    # Response body
    res = []
    for _group_id, _group_name, _members in zip(group_id_list, group_name_list, group_dict.values()):
        for member in _members:
            group_id = SelectedCourseSchema.SelectedCourseUpdate(group_id=_group_id)
            await SelectedCourseCrud.update(member["uid"], course_id, group_id)

        res.append({
            "group_id": _group_id,
            "group_name": _group_name,
            "members": _members
        })

    return res


@router.get(
    "/groups",
    response_model=list[GroupSchema.GroupRead],
    status_code=status.HTTP_200_OK
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
    "/group/{group_id}", 
    response_model=GroupSchema.GroupRead,
    status_code=status.HTTP_200_OK
)
async def get_group(group_id: str):
    group = await GroupCrud.get(group_id)
    if group:
        return group
    
    raise not_found

    
@router.put(
    "/group/{group_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_group(
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
