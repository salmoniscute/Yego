from fastapi import APIRouter, HTTPException, status

from crud.selected_course import SelectedCourseCrudManager
from schemas import selected_course as SelectedCourseSchema

SelectedCourseCrud = SelectedCourseCrudManager()
router = APIRouter(
    prefix="/api",
    tags=["Selected Course"]
)


@router.post(
    "/selected_course", 
    response_model=SelectedCourseSchema.SelectedCourseCreateResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_selected_course(newRow: SelectedCourseSchema.SelectedCourseCreate):
    """
    Create a selected course row with the following information:
    - **uid**
    - **course_id**
    - **group**
    """
    row = await SelectedCourseCrud.get_particular_selected_course(newRow.uid, newRow.course_id)
    if row:
        raise HTTPException(status_code=409, detail=f"Selected course already exists")
    
    row = await SelectedCourseCrud.create_selected_course(newRow)

    return row


@router.get(
    "/selected_course/user/{uid}", 
    response_model=list[SelectedCourseSchema.SelectedCourseRead]
)
async def get_all_selected_course_for_one_user(uid: str):
    """
    Get the list of selected course of the particular user
    """
    row_list = await SelectedCourseCrud.get_selected_course_by_uid(uid)
    if row_list:
        return row_list
    
    raise HTTPException(status_code=404, detail=f"User does not exist")
    

@router.get(
    "/selected_course/course/{course_id}", 
    response_model=list[SelectedCourseSchema.SelectedCourseRead]
)
async def get_all_users_for_one_course(course_id: str):
    """
    Get the list of members of the particular course
    """
    row_list = await SelectedCourseCrud.get_selected_course_by_course_id(course_id)
    if row_list:
        return row_list
    
    raise HTTPException(status_code=404, detail=f"Course does not exist")


@router.put(
    "/selected_course/{uid}/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_selected_course(updateRow: SelectedCourseSchema.SelectedCourseUpdate, uid: str, course_id: str):
    """
    Update the information of the particular selected course:
    - **group**
    """
    row = await SelectedCourseCrud.get_particular_selected_course(uid, course_id)
    if not row:
        raise HTTPException(status_code=404, detail="Selected course does not exist")
    
    await SelectedCourseCrud.update_selected_course_by_id(uid, course_id, updateRow)
    return 


@router.delete(
    "/selected_course/{uid}/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_selected_course(uid: str, course_id: str):
    """
    Delete the particular selected course.
    """
    row = await SelectedCourseCrud.get_particular_selected_course(uid, course_id)
    if not row:
        raise HTTPException(status_code=404, detail="Selected course does not exist")
    
    await SelectedCourseCrud.delete_selected_course_by_id(uid, course_id)
    return 
