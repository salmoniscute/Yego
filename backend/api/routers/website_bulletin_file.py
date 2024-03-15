from fastapi import APIRouter, Depends, HTTPException, status

from .depends import check_website_bulletin_file_id
from crud.website_bulletin_file import WebsiteBulletinFileCrudManager
from schemas import website_bulletin_file as WebsiteBulletinFileSchema

WebsiteBulletinFileCrud = WebsiteBulletinFileCrudManager()
router = APIRouter(
    prefix="/api",
    tags=["Website Bulletin File"]
)


@router.post(
    "/website_bulletin_file", 
    response_model=WebsiteBulletinFileSchema.WebsiteBulletinFileCreateResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_website_bulletin_file(newFile: WebsiteBulletinFileSchema.WebsiteBulletinFileCreate):
    """
    Create a website bulletin file with the following information:
    - **file_id**
    - **wb_id**
    - **path**
    """
    file = await WebsiteBulletinFileCrud.get_file_by_file_id(newFile.file_id)
    if file:
        raise HTTPException(status_code=409, detail=f"Website bulletin file already exists")
    
    file = await WebsiteBulletinFileCrud.create_file(newFile)
    return file


@router.get(
    "/website_bulletin_file/{file_id}", 
    response_model=WebsiteBulletinFileSchema.WebsiteBulletinFileRead
)
async def get_website_bulletin_file(file_id: str):
    """
    Get the information of the particular website bulletin file.
    """
    file = await WebsiteBulletinFileCrud.get_file_by_file_id(file_id)
    if file:
        return file
    
    raise HTTPException(status_code=404, detail=f"Website bulletin file does not exist")
    

@router.put(
    "/website_bulletin_file/{file_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_website_bulletin_file(updateFile: WebsiteBulletinFileSchema.WebsiteBulletinFileUpdate, file_id: str = Depends(check_website_bulletin_file_id)):
    """
    Update the information of the particular website bulletin file with the following information:
    - **path**
    """
    await WebsiteBulletinFileCrud.update_file_by_file_id(file_id, updateFile)
    return 


@router.delete(
    "/website_bulletin_file/{file_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_website_bulletin_file(file_id: str = Depends(check_website_bulletin_file_id)):
    """
    Delete the particular website bulletin file.
    """
    await WebsiteBulletinFileCrud.delete_file_by_file_id(file_id)
    return 
