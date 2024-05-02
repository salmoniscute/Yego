from fastapi import APIRouter, Depends, HTTPException, status

from .depends import check_course_id, check_user_id
from crud.course import CourseCrudManager
from schemas import course as CourseSchema

not_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Course does not exist"
)

already_exists = HTTPException(
    status_code=status.HTTP_409_CONFLICT, 
    detail="Course already exists"
)

CourseCrud = CourseCrudManager()
router = APIRouter(
    tags=["Course"],
    prefix="/api"
)


@router.post(
    "/course", 
    status_code=status.HTTP_204_NO_CONTENT,
    response_description="The course has been successfully created."
)
async def create_course(
    newCourse: CourseSchema.CourseCreate,
    uid: str = Depends(check_user_id)
):
    """
    Create a user with the following information:
    - **course_id**
    - **uid**
    - **course_code**
    - **academic_year**
    - **semester**
    - **name**
    - **outline**
    """
    course = await CourseCrud.get(newCourse.id)
    if course:
        raise already_exists
    
    # create course
    course = await CourseCrud.create(uid, newCourse)

    return course


@router.get(
    "/courses",
    response_model=list[CourseSchema.CourseRead],
    status_code=status.HTTP_200_OK,
    response_description="Get all courses"
)
async def get_all_courses():
    """ 
    Get all courses.
    """
    courses = await CourseCrud.get_all()
    if courses:
        return courses
    raise not_found


@router.get(
    "/course/{course_id}", 
    response_model=CourseSchema.CourseRead,
    status_code=status.HTTP_200_OK,
    response_description="Get a couse",  
)
async def get_course(course_id: str = None):
    course = await CourseCrud.get(course_id)
    if course:
        return course
    
    raise not_found

    
@router.put(
    "/course/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_course(
    updateCourse: CourseSchema.CourseUpdate,
    course_id: str = Depends(check_course_id)
):
    """ 
    Update the particular course with at least one of the following information:
    - **instructor**
    - **course_code**
    - **academic_year**
    - **semester**
    - **name**
    - **outline**
    """
    await CourseCrud.update(course_id, updateCourse)

    return 


@router.delete(
    "/course/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT 
)
async def delete_course(course_id: str = Depends(check_course_id)):
    """ 
    Delete the course.
    """
    await CourseCrud.delete(course_id)
    
    return 
