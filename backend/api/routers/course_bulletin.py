from fastapi import APIRouter, HTTPException, status, Depends
from crud.course_bulletin import CourseBulletinCrudManager
from schemas import course_bulletin as CourseBulletinSchema
from .depends import check_course_bulletin_id

CourseBulletinCrud = CourseBulletinCrudManager()
router = APIRouter(
    tags=["Course Bulletin"],
    prefix="/api"
)

@router.post(
    "/course_bulletin", 
    response_model=CourseBulletinSchema.CourseBulletinCreate,
    status_code=201,
    response_description="The bulletin has been successfully created."
)
async def create_course_bulletin(newCourseBulletin: CourseBulletinSchema.CourseBulletinCreate):
    """
    Create a bulletin with the following information:
    - **cb_id**
    - **publisher**
    - **course_id**
    - **title**
    - **release_time**
    - **content**
    """
    
    
    course_bulletin = await CourseBulletinCrud.get_course_bulletin_by_cb_id(newCourseBulletin.cb_id)
    if course_bulletin:
        raise HTTPException(status_code=409, detail=f"Bulletin already exists")
    
    # create bulletin
    course_bulletin = await CourseBulletinCrud.create_course_bulletin(newCourseBulletin)

    return course_bulletin

@router.get(
    "/course_bulletin", 
    response_model=CourseBulletinSchema.CourseBulletinRead,
    response_description="Get a couse",  
)
async def get_course_bulletin(cb_id: str = None):

    course_bulletin = await CourseBulletinCrud.get_course_bulletin_by_cb_id(cb_id)
    
    if course_bulletin:
        return course_bulletin
    raise HTTPException(status_code=404, detail=f"Bulletin doesn't exist")
    

@router.put(
    "/course_bulletin/{cb_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_course_bulletin(newBulletinCourse: CourseBulletinSchema.CourseBulletinUpdate, cb_id: str = Depends(check_course_bulletin_id)):
    await CourseBulletinCrud.update_course_bulletin_by_id(cb_id, newBulletinCourse)
    return 

@router.delete(
    "/course_bulletin/{cd_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_course(cb_id: str = Depends(check_course_bulletin_id)):

    await CourseBulletinCrud.delete_course_bulletin_by_id(cb_id)
    
    return 