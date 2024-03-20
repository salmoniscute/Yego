from fastapi import APIRouter, Depends, HTTPException, status

from .depends import check_website_bulletin_file_id
from crud.website_bulletin_file import WebsiteBulletinFileCrudManager
from schemas import website_bulletin_file as WebsiteBulletinFileSchema

already_exists = HTTPException(
    status_code=status.HTTP_409_CONFLICT, 
    detail="Website bulletin file already exists"
)

not_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, 
    detail="Website bulletin file does not exist"
)

WebsiteBulletinFileCrud = WebsiteBulletinFileCrudManager()
router = APIRouter(
    prefix="/api",
    tags=["Website Bulletin File"]
)


@router.post(
    "/website_bulletin_file", 
    response_model=WebsiteBulletinFileSchema.WebsiteBulletinFileRead,
    status_code=status.HTTP_201_CREATED
)
async def create_website_bulletin_file(newFile: WebsiteBulletinFileSchema.WebsiteBulletinFileCreate):
    """
    Create a website bulletin file with the following information:
    - **file_id**
    - **wb_id**
    - **path**
    """
    if await WebsiteBulletinFileCrud.get(newFile.file_id):
        raise already_exists
    
    file = await WebsiteBulletinFileCrud.create(newFile)
    return file


@router.get(
    "/website_bulletin_files", 
    response_model=list[WebsiteBulletinFileSchema.WebsiteBulletinFileRead],
    status_code=status.HTTP_200_OK
)
async def get_all_website_bulletin_files():
    """
    Get all website bulletin files.
    """
    files = await WebsiteBulletinFileCrud.get_all()
    if files:
        return files
    
    raise not_found


@router.get(
    "/website_bulletin_file/{file_id}", 
    response_model=WebsiteBulletinFileSchema.WebsiteBulletinFileRead
)
async def get_website_bulletin_file(file_id: str):
    """
    Get the website bulletin file.
    """
    file = await WebsiteBulletinFileCrud.get(file_id)
    if file:
        return file
    
    raise not_found
    

@router.put(
    "/website_bulletin_file/{file_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_website_bulletin_file(
    updateFile: WebsiteBulletinFileSchema.WebsiteBulletinFileUpdate, 
    file_id: str = Depends(check_website_bulletin_file_id)
):
    """
    Update the website bulletin file with the following information:
    - **path**
    """
    await WebsiteBulletinFileCrud.update(file_id, updateFile)
    return 


@router.delete(
    "/website_bulletin_file/{file_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_website_bulletin_file(file_id: str = Depends(check_website_bulletin_file_id)):
    """
    Delete the website bulletin file.
    """
    await WebsiteBulletinFileCrud.delete(file_id)
    return 
