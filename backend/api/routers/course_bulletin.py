from fastapi import APIRouter, Depends, HTTPException, status

from .depends import check_course_id, check_course_bulletin_id, check_user_id
from crud.course_bulletin import CourseBulletinCrudManager
from crud.notification import NotificationCrudManager
from crud.selected_course import SelectedCourseCrudManager
from schemas import bulletin as BulletinSchema

not_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, 
    detail="Course bulletin does not exist"
)

already_exists = HTTPException(
    status_code=status.HTTP_409_CONFLICT, 
    detail="Course bulletin already exists"
)

CourseBulletinCrud = CourseBulletinCrudManager()
router = APIRouter(
    prefix="/api/course",
    tags=["Course Bulletin"]
)

NotificationCrud = NotificationCrudManager()
SelectedCourseCrud = SelectedCourseCrudManager()

@router.post(
    "/bulletin", 
    status_code=status.HTTP_204_NO_CONTENT
)
async def create_course_bulletin(
    newBulletin: BulletinSchema.BulletinCreate,
    uid: str = Depends(check_user_id),
    course_id: str = Depends(check_course_id)
):
    """
    Create a bulletin with the following information:
    - **release_time**
    - **title**
    - **content**
    - **pin_to_top**
    """
    bulletin = await CourseBulletinCrud.create(uid, course_id, newBulletin)
    users = await SelectedCourseCrud.get_by_course_id(course_id)
    for user in users:
        await NotificationCrud.create(user["uid"], bulletin.id, "course_bulletin")
        
    return bulletin


@router.get(
    "/bulletin/{cb_id}", 
    response_model=BulletinSchema.BulletinReadByID,
    status_code=status.HTTP_200_OK
)
async def get_course_bulletin(cb_id: int):
    """
    Get the course bulletin.
    """
    bulletin = await CourseBulletinCrud.get(cb_id)
    if bulletin:
        return bulletin

    raise not_found


@router.get(
    "/bulletin/particular_course/{course_id}", 
    response_model=list[BulletinSchema.CourseBulletinListRead],
    status_code=status.HTTP_200_OK
)
async def get_all_course_bulletins_in_particular_course(
    uid: str = Depends(check_user_id), 
    course_id: int = Depends(check_course_id)
):
    """
    Get all course bulletins in particular course and the subscription status of user.
    """
    bulletins = await CourseBulletinCrud.get_by_course_id(uid, course_id)
    if bulletins:
        return bulletins
    
    raise not_found
   

@router.put(
    "/bulletin/{cb_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_course_bulletin(
    updateBulletin: BulletinSchema.BulletinUpdate, 
    cb_id: int = Depends(check_course_bulletin_id)
):
    """
    Update the particular course bulletin with at least one of the following information:
    - **title**
    - **content**
    - **pin_to_top**
    """
    await CourseBulletinCrud.update(cb_id, updateBulletin)
    bulletin = await CourseBulletinCrud.get(cb_id)
    
    users = await SelectedCourseCrud.get_by_course_id(bulletin["course_id"])
    for user in users:
        await NotificationCrud.create(user["uid"], cb_id, "course_bulletin")
    
    return 


@router.delete(
    "/bulletin/{cb_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_course_bulletin(cb_id: int = Depends(check_course_bulletin_id)):
    """
    Delete the course bulletin.
    """
    await CourseBulletinCrud.delete(cb_id)
    return 
