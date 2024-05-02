from fastapi import APIRouter, Depends, HTTPException, status

from .depends import check_component_id, check_user_id
from crud.website_bulletin import WebsiteBulletinCrudManager
from schemas import bulletin as BulletinSchema

not_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, 
    detail="Website bulletin does not exist"
)

already_exists = HTTPException(
    status_code=status.HTTP_409_CONFLICT, 
    detail="Website bulletin already exists"
)

WebsiteBulletinCrud = WebsiteBulletinCrudManager()
router = APIRouter(
    prefix="/api/website",
    tags=["Website Bulletin"]
)


@router.post(
    "/bulletin", 
    status_code=status.HTTP_204_NO_CONTENT
)
async def create_website_bulletin(
    newBulletin: BulletinSchema.BulletinCreate,
    uid: str = Depends(check_user_id)
):
    """
    Create a bulletin with the following information:
    - **id**
    - **release_time**
    - **title**
    - **content**
    - **pin_to_top**
    """
    await WebsiteBulletinCrud.create(uid, newBulletin)
    return


@router.get(
    "/bulletins", 
    response_model=list[BulletinSchema.BulletinListRead],
    status_code=status.HTTP_200_OK
)
async def get_all_website_bulletins():
    """
    Get all website bulletins.
    """
    bulletins = await WebsiteBulletinCrud.get_all()
    if bulletins:
        return bulletins
    
    raise not_found


@router.get(
    "/bulletin/{wb_id}", 
    response_model=BulletinSchema.BulletinReadByID,
    status_code=status.HTTP_200_OK
)
async def get_website_bulletin(wb_id: str):
    """
    Get the website bulletin.
    """
    bulletin = await WebsiteBulletinCrud.get(wb_id)
    if bulletin:
        return bulletin

    raise not_found
   

@router.put(
    "/bulletin/{wb_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_website_bulletin(
    updateBulletin: BulletinSchema.BulletinUpdate, 
    wb_id: str = Depends(check_component_id)
):
    """
    Update the particular website bulletin with at least one of the following information:
    - **title**
    - **content**
    - **pin_to_top**
    """
    await WebsiteBulletinCrud.update(wb_id, updateBulletin)
    return 


@router.delete(
    "/bulletin/{wb_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_website_bulletin(wb_id: str = Depends(check_component_id)):
    """
    Delete the website bulletin.
    """
    await WebsiteBulletinCrud.delete(wb_id)
    return 
