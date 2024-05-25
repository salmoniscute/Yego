from fastapi import APIRouter, Depends, HTTPException, status

from .depends import check_course_id, check_group_id, check_user_id
from crud.selected_course import SelectedCourseCrudManager
from schemas import selected_course as SelectedCourseSchema

not_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, 
    detail="Selected course does not exist"
)

already_exists = HTTPException(
    status_code=status.HTTP_409_CONFLICT, 
    detail="Selected course already exists"
)

SelectedCourseCrud = SelectedCourseCrudManager()
router = APIRouter(
    prefix="/api",
    tags=["Selected Course"]
)


@router.post(
    "/selected_course", 
    status_code=status.HTTP_204_NO_CONTENT
)
async def create_selected_course(
    uid: str = Depends(check_user_id),
    course_id: int = Depends(check_course_id)
):
    """
    Create a selected course row.
    """
    if await SelectedCourseCrud.get(uid, course_id):
        raise already_exists
    
    await SelectedCourseCrud.create(uid, course_id)
    return 


@router.get(
    "/selected_course/user/{uid}", 
    response_model=list[SelectedCourseSchema.SelectedCourseByUidRead],
    status_code=status.HTTP_200_OK
)
async def get_selected_courses_by_uid(uid: str):
    """
    Get the selected course by uid.
    """
    selected_courses = await SelectedCourseCrud.get_by_uid(uid)
    if selected_courses:
        return selected_courses
    
    raise not_found


@router.get(
    "/selected_course/course/{course_id}", 
    response_model=list[SelectedCourseSchema.SelectedCourseByCourseIdRead],
    status_code=status.HTTP_200_OK
)
async def get_selected_courses_by_course_id(course_id: int):
    """
    Get the selected course by course_id.
    """
    selected_courses = await SelectedCourseCrud.get_by_course_id(course_id)
    if selected_courses:
        return selected_courses
    
    raise not_found


@router.get(
    "/selected_course/particular/{uid}/{course_id}", 
    status_code=status.HTTP_200_OK
)
async def get_user_group(
    uid: str = Depends(check_user_id),
    course_id: int = Depends(check_course_id)
):
    """
    Get the group of particular user in this course.
    """
    selected_course = await SelectedCourseCrud.get(uid, course_id)
    if selected_course:
        if selected_course.group_info:
            return selected_course.group_info.name
        else:
            return None
    
    raise not_found


@router.delete(
    "/selected_course/particular/{uid}/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_selected_course(
    uid: str = Depends(check_user_id),
    course_id: int = Depends(check_course_id)
):
    """
    Delete the selected course.
    """
    await SelectedCourseCrud.delete(uid, course_id)
    return 
