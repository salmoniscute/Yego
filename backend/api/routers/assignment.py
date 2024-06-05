from fastapi import APIRouter, HTTPException, status, Depends

from .depends import check_assignment_id, check_user_id, check_course_material_id
from crud.course_material import CourseMaterialCrudManager
from crud.assignment import AssignmentCrudManager
from crud.notification import NotificationCrudManager
from crud.selected_course import SelectedCourseCrudManager
from schemas import course_material as CourseMaterialSchema

not_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, 
    detail="Assignment does not exist"
)

already_exists = HTTPException(
    status_code=status.HTTP_409_CONFLICT, 
    detail="Assignment already exists"
)

AssignmentCrud = AssignmentCrudManager()
CourseMaterialCrud = CourseMaterialCrudManager()
NotificationCrud = NotificationCrudManager()
SelectedCourseCrud = SelectedCourseCrudManager()

router = APIRouter(
    tags=["Assignment"],
    prefix="/assignment"
)


@router.post(
    "", 
    status_code=status.HTTP_201_CREATED
)
async def create_assignment(
    newAssignment: CourseMaterialSchema.AssignmentCreate,
    uid: str = Depends(check_user_id),
    course_material_id: int = Depends(check_course_material_id)
):
    material_info = await AssignmentCrud.create(uid, course_material_id, newAssignment)

    # course_material = await CourseMaterialCrud.get(course_material_id)  
    # users = await SelectedCourseCrud.get_by_course_id(course_material[0].course_id)
    # for user in users:
    #     await NotificationCrud.create(user["uid"], material_info.id, "assignment")

    return {"id": material_info.id}


@router.put(
    "/{assignment_id}", 
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_assignment(
    newAssignment: CourseMaterialSchema.AssignmentUpdate,
    assignment_id: int = Depends(check_assignment_id)
):
    await AssignmentCrud.update(assignment_id, newAssignment)

    # material_info = await AssignmentCrud.get(assignment_id)
    # course_material = await CourseMaterialCrud.get(material_info[0].material_id)  
    # users = await SelectedCourseCrud.get_by_course_id(course_material[0].course_id)
    # for user in users:
    #     await NotificationCrud.create(user["uid"], material_info[0].id, "assignment")

    return


@router.delete(
    "/{assignment_id}", 
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_assignment(
    assignment_id: int = Depends(check_assignment_id)
):
    await AssignmentCrud.delete(assignment_id)
    return
