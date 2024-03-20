from fastapi import APIRouter, HTTPException, status, Depends
from crud.course import CourseCrudManager
from schemas import course as CourseSchema
from .depends import check_course_id

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
async def create_course(newCourse: CourseSchema.CourseCreate):
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
    
    
    course = await CourseCrud.get_course_by_id(newCourse.course_id)
    if course:
        raise HTTPException(status_code=409, detail=f"Course already exists")
    
    # create course
    course = await CourseCrud.create_course(newCourse)

    return course

@router.get(
    "/course", 
    response_model=CourseSchema.CourseRead,
    response_description="Get a couse",  
)
async def get_course(course_id: str = None):

    course = await CourseCrud.get_course_by_id(course_id)
    
    if course:
        return course
    raise HTTPException(status_code=404, detail=f"Course doesn't exist")
    

@router.put(
    "/course/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_course(newCourse: CourseSchema.CourseUpdate, course_id: str = Depends(check_course_id)):
    
    
    await CourseCrud.update_course_by_id(course_id, newCourse)

    return 

@router.delete(
    "/course/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT 
)
async def delete_course(course_id: str = Depends(check_course_id)):

    await CourseCrud.delete_course_by_id(course_id)
    
    return 