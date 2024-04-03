from fastapi import APIRouter, Depends, HTTPException, status

from .depends import check_user_id, check_course_id
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
    response_model=SelectedCourseSchema.SelectedCourseRead,
    status_code=status.HTTP_201_CREATED
)
async def create_selected_course(
    newRow: SelectedCourseSchema.SelectedCourseCreate,
    uid: str = Depends(check_user_id),
    course_id: str = Depends(check_course_id)
):
    """
    Create a selected course row with the following information:
    - **uid** (should be existing)
    - **course_id** (should be existing)
    - **group**
    """
    if await SelectedCourseCrud.get(uid, course_id):
        raise already_exists
    
    selected_course = await SelectedCourseCrud.create(uid, course_id, newRow)
    return selected_course


@router.get(
    "/selected_courses", 
    response_model=list[SelectedCourseSchema.SelectedCourseRead],
    status_code=status.HTTP_200_OK
)
async def get_all_selected_courses():
    """
    Get all selected courses.
    """
    selected_courses = await SelectedCourseCrud.get_all()
    if selected_courses:
        return selected_courses
    
    raise not_found


@router.get(
    "/selected_course/particular/{uid}/{course_id}", 
    response_model=SelectedCourseSchema.SelectedCourseRead,
    status_code=status.HTTP_200_OK
)
async def get_selected_courses(uid: str, course_id: str):
    """
    Get the particular selected course.
    """
    selected_course = await SelectedCourseCrud.get(uid, course_id)
    if selected_course:
        return selected_course
    
    raise not_found


@router.put(
    "/selected_course/particular/{uid}/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_selected_course(
    updateRow: SelectedCourseSchema.SelectedCourseUpdate,
    uid: str = Depends(check_user_id),
    course_id: str = Depends(check_course_id)
):
    """
    Update the information of the particular selected course:
    - **group**
    """
    await SelectedCourseCrud.update(uid, course_id, updateRow)
    return 


@router.delete(
    "/selected_course/particular/{uid}/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_selected_course(
    uid: str = Depends(check_user_id),
    course_id: str = Depends(check_course_id)
):
    """
    Delete the selected course.
    """
    await SelectedCourseCrud.delete(uid, course_id)
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
    results= []

    selected_courses = await SelectedCourseCrud.get_by_uid(uid)
    print(selected_courses)
    if selected_courses:
        for selected_course in selected_courses:
            result = {
                "course_name": selected_course.course_info.name,
                "instructor_name": selected_course.course_info.instructor_info.name
            }
            results.append(result)
            
        return results
    
    raise not_found


@router.get(
    "/selected_course/course/{course_id}", 
    response_model=list[SelectedCourseSchema.SelectedCourseByCourseIdRead],
    status_code=status.HTTP_200_OK
)
async def get_selected_courses_by_course_id(course_id: str):
    """
    Get the selected course by course_id.
    """
    results = []

    selected_courses = await SelectedCourseCrud.get_by_course_id(course_id)
    if selected_courses:
        for selected_course in selected_courses:
            result = {
                "name": selected_course.user_info.name,
                "uid": selected_course.user_info.uid,
                "department": selected_course.user_info.department,
                "role": selected_course.user_info.role,
                "group": selected_course.group
            }
            results.append(result)

        return results
    
    raise not_found
