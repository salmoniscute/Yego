from fastapi import APIRouter, Depends, HTTPException, status

from .depends import check_user_id, check_website_bulletin_id
from crud.website_bulletin import WebsiteBulletinCrudManager
from schemas import website_bulletin as WebsiteBulletinSchema

already_exists = HTTPException(
    status_code=409, 
    detail="Website bulletin already exists"
)

not_found = HTTPException(
    status_code=404, 
    detail="Website bulletin does not exist"
)

WebsiteBulletinCrud = WebsiteBulletinCrudManager()
router = APIRouter(
    prefix="/api",
    tags=["Website Bulletin"]
)


@router.post(
    "/website_bulletin", 
    response_model=WebsiteBulletinSchema.WebsiteBulletinCreateResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_website_bulletin(
    newBulletin: WebsiteBulletinSchema.WebsiteBulletinCreate,
    publisher: str = Depends(check_user_id)
):
    """
    Create a website bulletin with the following information:
    - **publisher** (alias of uid, should be existing)
    - **wb_id**
    - **title**
    - **release_time**
    - **content**
    - **pin_to_top**
    """
    if await WebsiteBulletinCrud.get(newBulletin.wb_id):
        raise already_exists
    
    website_bulletin = await WebsiteBulletinCrud.create(publisher, newBulletin)
    return website_bulletin


@router.get(
    "/website_bulletins", 
    response_model=list[WebsiteBulletinSchema.WebsiteBulletinRead],
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
    "/website_bulletin/{wb_id}", 
    response_model=WebsiteBulletinSchema.WebsiteBulletinRead,
    status_code=status.HTTP_200_OK
)
async def get_website_bulletin(wb_id: str):
    """
    Get the particular website bulletin.
    """
    bulletin = await WebsiteBulletinCrud.get(wb_id)
    if bulletin:
        return bulletin
    
    raise not_found
   

@router.put(
    "/website_bulletin/{wb_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_website_bulletin(
    updateBulletin: WebsiteBulletinSchema.WebsiteBulletinUpdate, 
    wb_id: str = Depends(check_website_bulletin_id)
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
    "/website_bulletin/{wb_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_website_bulletin(wb_id: str = Depends(check_website_bulletin_id)):
    """
    Delete the website bulletin.
    """
    await WebsiteBulletinCrud.delete(wb_id)
    return 
