from fastapi import APIRouter, Depends, HTTPException, status, UploadFile

from .depends import check_component_id
from crud.file import FileCrudManager
from schemas import file as FileSchema
import os
not_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Component does not exist"
)

already_exists = HTTPException(
    status_code=status.HTTP_409_CONFLICT, 
    detail="Component already exists"
)

FileCrud = FileCrudManager()
router = APIRouter(
    tags=["File"],
    prefix="/api"
)


@router.post(
    "/file", 
    status_code=status.HTTP_201_CREATED,
    response_description="The file has been successfully created."
)
async def create_files(
    files: list[UploadFile],
    component_id: str = Depends(check_component_id)
):
    out_file_path = f"upload/component/{component_id}/"
    if not os.path.isdir(out_file_path):
            os.makedirs(out_file_path)
    for file in files:
        with open(out_file_path + file.filename, 'wb') as out_file:
            file_path = "backend/" + out_file_path + file.filename
            content = await file.read()  
            out_file.write(content) 
            file = await FileCrud.create(component_id=component_id, path=file_path)

    return
    

@router.get(
    "/files",
    response_model=list[FileSchema.FileRead],
    status_code=status.HTTP_200_OK,
    response_description="Get all files",
    deprecated=True
)
async def get_all_files():
    """ 
    Get all files.
    """
    files = await FileCrud.get_all()
    if not files:
        raise not_found
    
    return files


@router.get(
    "/file/{file_id}",
    response_model=FileSchema.FileRead,
    status_code=status.HTTP_200_OK,
    response_description="Get a file",
    deprecated=True
)
async def get_file(file_id: str):
    """
    Get a file.
    """
    file = await FileCrud.get(file_id)
    if not file:
        raise not_found
    
    return file



@router.delete(
    "/file/{file_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_description="The file has been successfully deleted."
)
async def delete_file(file_id: str):
    """
    Delete a file.
    """
    file = await FileCrud.get(file_id)
    if not file:
        raise not_found
    
    await FileCrud.delete(file_id)

    return



