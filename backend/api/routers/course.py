from fastapi import APIRouter, HTTPException, status, Depends
from crud.course import CourseCrudManager
from schemas import course as CourseSchema
from .depends import check_course_id, check_user_id

from schemas import course_bulletin as CourseBulletinSchema

CourseCrud = CourseCrudManager()
router = APIRouter(
    tags=["Course"],
    prefix="/api"
)

@router.post(
    "/course", 
    response_model=CourseSchema.CourseCreate,
    status_code=201,
    response_description="The course has been successfully created."
)
async def create_course(
    newCourse: CourseSchema.CourseCreate,
    teacher: str = Depends(check_user_id)
    ):
    """
    Create a user with the following information:
    - **course_id**
    - **teacher**
    - **course_code**
    - **academic_year**
    - **semester**
    - **name**
    - **outline**
    """
    
    
    course = await CourseCrud.get(newCourse.course_id)
    if course:
        raise HTTPException(status_code=409, detail=f"Course already exists")
    
    # create course
    course = await CourseCrud.create(teacher, newCourse)

    return course

@router.get(
    "/courses",
    response_model=list[CourseSchema.CourseRead],
    status_code=200,
    response_description="Get all courses"
)
async def get_all_courses():
    """ 
    Get all courses.
    """
    courses = await CourseCrud.get_all()
    if courses:
        return courses
    raise HTTPException(status_code=404, detail=f"No courses found")


@router.get(
    "/course/{course_id}", 
    response_model=CourseSchema.CourseRead,
    status_code=200,
    response_description="Get a couse",  
)
async def get_course(course_id: str = None):

    course = await CourseCrud.get(course_id)
    
    if course:
        return course
    raise HTTPException(status_code=404, detail=f"Course doesn't exist")
    
@router.get(
    "/course/{course_id}/bulletins",
    response_model=list[CourseBulletinSchema.CourseBulletinRead],
    status_code=200,
    response_description="Get a list of bulletins of the course.",  
)
async def get_course_bulletins(course_id: str = None):
    """ 
    Get a list of bulletins of the course.
    """
    course = await CourseCrud.get(course_id)
    if course:
        return course.bulletins
    raise HTTPException(status_code=404, detail=f"Course doesn't exist")

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
    - **teacher**
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