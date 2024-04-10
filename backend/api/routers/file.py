from fastapi import APIRouter, Depends, HTTPException, status

from .depends import check_component_id
from crud.file import FileCrudManager
from schemas import file as FileSchema

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
    response_model=FileSchema.FileRead,
    status_code=status.HTTP_201_CREATED,
    response_description="The file has been successfully created."
)
async def create_file(
    newFile: FileSchema.FileCreate,
    component_id: str = Depends(check_component_id)
):
    """
    Create a file with the following information:
    - **path**
    """
    file = await FileCrud.create(component_id=component_id, newFile=newFile)

    return file
    

@router.get(
    "/files",
    response_model=list[FileSchema.FileRead],
    status_code=status.HTTP_200_OK,
    response_description="Get all files"
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
    response_description="Get a file"
)
async def get_file(file_id: str):
    """
    Get a file.
    """
    file = await FileCrud.get(file_id)
    if not file:
        raise not_found
    
    return file


@router.put(
    "/file/{file_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_description="The file has been successfully updated."
)
async def update_file(
    file_id: str,
    updateFile: FileSchema.FileUpdate
):
    """
    Update a file.
    """
    await FileCrud.update(file_id, updateFile)

    return


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
