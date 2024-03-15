from fastapi import APIRouter, Depends, HTTPException, status

from .depends import check_website_bulletin_id
from crud.website_bulletin import WebsiteBulletinCrudManager
from schemas import website_bulletin as WebsiteBulletinSchema

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
async def create_website_bulletin(newBulletin: WebsiteBulletinSchema.WebsiteBulletinCreate):
    """
    Create a website bulletin with the following information:
    - **wb_id**
    - **publisher**
    - **title**
    - **release_time**
    - **content**
    - **pin_to_top**
    """
    website_bulletin = await WebsiteBulletinCrud.get_website_bulletin_by_wb_id(newBulletin.wb_id)
    if website_bulletin:
        raise HTTPException(status_code=409, detail=f"Website bulletin already exists")
    
    website_bulletin = await WebsiteBulletinCrud.create_website_bulletin(newBulletin)
    return website_bulletin


@router.get(
    "/website_bulletin/{wb_id}", 
    response_model=WebsiteBulletinSchema.WebsiteBulletinRead
)
async def get_website_bulletin(wb_id: str):
    """
    Get the information of the particular website bulletin.
    """
    website_bulletin = await WebsiteBulletinCrud.get_website_bulletin_by_wb_id(wb_id)
    if website_bulletin:
        return website_bulletin
    
    raise HTTPException(status_code=404, detail=f"Website bulletin does not exist")
    

@router.put(
    "/website_bulletin/{wb_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_website_bulletin(updateBulletin: WebsiteBulletinSchema.WebsiteBulletinUpdate, wb_id: str = Depends(check_website_bulletin_id)):
    """
    Update the information of the particular website bulletin with at least one of the following information:
    - **title**
    - **content**
    - **pin_to_top**
    """
    await WebsiteBulletinCrud.update_website_bulletin_by_wb_id(wb_id, updateBulletin)
    return 


@router.delete(
    "/website_bulletin/{wb_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_website_bulletin(wb_id: str = Depends(check_website_bulletin_id)):
    """
    Delete the particular website bulletin.
    """
    await WebsiteBulletinCrud.delete_website_bulletin_by_wb_id(wb_id)
    return 