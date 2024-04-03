from fastapi import APIRouter, Depends, HTTPException, status

from .depends import check_user_id, check_course_id, check_course_bulletin_id
from crud.course_bulletin import CourseBulletinCrudManager
from schemas import course_bulletin as CourseBulletinSchema

not_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, 
    detail="Course Bulletin does not exist"
)

already_exists = HTTPException(
    status_code=status.HTTP_409_CONFLICT, 
    detail="Course Bulletin already exists"
)

CourseBulletinCrud = CourseBulletinCrudManager()
router = APIRouter(
    prefix="/api",
    tags=["Course Bulletin"]
)


@router.post(
    "/bulletin/course", 
    response_model=CourseBulletinSchema.CourseBulletinRead,
    status_code=status.HTTP_201_CREATED
)
async def create_course_bulletin(
    newBulletin: CourseBulletinSchema.CourseBulletinCreate,
    publisher: str = Depends(check_user_id),
    course_id: str = Depends(check_course_id)
):
    """
    Create a bulletin with the following information:
    - **id**
    - **release_time**
    - **title**
    - **content**
    - **pin_to_top**
    """
    if await CourseBulletinCrud.get(newBulletin.id):
        raise already_exists
    
    bulletin = await CourseBulletinCrud.create(publisher, course_id, newBulletin)
    return bulletin


# @router.get(
#     "/website_bulletins", 
#     response_model=list[WebsiteBulletinSchema.WebsiteBulletinRead],
#     status_code=status.HTTP_200_OK
# )
# async def get_all_website_bulletins():
#     """
#     Get all website bulletins.
#     """
#     bulletins = await WebsiteBulletinCrud.get_all()
#     if bulletins:
#         return bulletins
    
#     raise not_found


@router.get(
    "/bulletin/course/{bulletin_id}", 
    response_model=CourseBulletinSchema.CourseBulletinRead,
    status_code=status.HTTP_200_OK
)
async def get_course_bulletin(bulletin_id: str):
    """
    Get the website bulletin.
    """
    bulletin = await CourseBulletinCrud.get(bulletin_id)
    if bulletin:
        return bulletin
    
    raise not_found
   

# @router.put(
#     "/website_bulletin/{wb_id}",
#     status_code=status.HTTP_204_NO_CONTENT
# )
# async def update_website_bulletin(
#     updateBulletin: WebsiteBulletinSchema.WebsiteBulletinUpdate, 
#     wb_id: str = Depends(check_website_bulletin_id)
# ):
#     """
#     Update the particular website bulletin with at least one of the following information:
#     - **title**
#     - **content**
#     - **pin_to_top**
#     """
#     await WebsiteBulletinCrud.update(wb_id, updateBulletin)
#     return 


# @router.delete(
#     "/website_bulletin/{wb_id}",
#     status_code=status.HTTP_204_NO_CONTENT
# )
# async def delete_website_bulletin(wb_id: str = Depends(check_website_bulletin_id)):
#     """
#     Delete the website bulletin.
#     """
#     await WebsiteBulletinCrud.delete(wb_id)
#     return 
