from fastapi import APIRouter, HTTPException, status, Depends
from crud.course_bulletin import CourseBulletinCrudManager
from schemas import course_bulletin as CourseBulletinSchema
from .depends import check_course_bulletin_id, check_course_id

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
async def create_course_bulletin(
    newCourseBulletin: CourseBulletinSchema.CourseBulletinCreate,
    course_id: str = Depends(check_course_id)
):
    """
    Create a bulletin with the following information:
    - **cb_id**
    - **publisher**
    - **course_id** ( should be existed )
    - **title**
    - **release_time**
    - **content**
    - **pin_to_top**
    """
    
    
    course_bulletin = await CourseBulletinCrud.get(newCourseBulletin.cb_id)
    if course_bulletin:
        raise HTTPException(status_code=409, detail=f"Bulletin already exists")
    
    # create bulletin
    course_bulletin = await CourseBulletinCrud.create(course_id, newCourseBulletin)

    return course_bulletin


@router.get(
    "/course_bulletins",
    response_model=list[CourseBulletinSchema.CourseBulletinRead],
    response_description="Get all bulletins"
)
async def get_all_course_bulletins():
    """ 
    Get all course bulletins.
    """
    course_bulletins = await CourseBulletinCrud.get_all()
    if course_bulletins:
        return course_bulletins
    raise HTTPException(status_code=404, detail=f"No bulletins found")

@router.get(
    "/course_bulletin/{cb_id}", 
    response_model=CourseBulletinSchema.CourseBulletinRead,
    response_description="Get a course bulletin",  
)
async def get_course_bulletin(cb_id: str):
    """ 
    Get a course bulletin.
    """
    course_bulletin = await CourseBulletinCrud.get(cb_id)
    
    if course_bulletin:
        return course_bulletin
    raise HTTPException(status_code=404, detail=f"Bulletin doesn't exist")
    

@router.put(
    "/course_bulletin/{cb_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_course_bulletin(
    updateCourseBulletin: CourseBulletinSchema.CourseBulletinUpdate,
    cb_id: str = Depends(check_course_bulletin_id)
):
    """ 
    Update a course bulletin with the following information:
    - **title**
    - **release_time**
    - **content**
    """
    await CourseBulletinCrud.update(cb_id, updateCourseBulletin)
    return 

@router.delete(
    "/course_bulletin/{cd_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_course_bulletin(cb_id: str = Depends(check_course_bulletin_id)):
    """ 
    Delete a course bulletin.
    """
    await CourseBulletinCrud.delete(cb_id)
    
    return 