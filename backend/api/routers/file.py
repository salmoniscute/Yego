import os
from fastapi import APIRouter, Depends, HTTPException, status, UploadFile

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
    status_code=status.HTTP_204_NO_CONTENT,
    response_description="The file has been successfully created."
)
async def create_files(
    files: list[UploadFile],
    component_id: int = Depends(check_component_id)
):
    public_dir = "../frontend/public"
    component_dir = f"assets/upload/component/{component_id}"
    if not os.path.isdir(f"{public_dir}/{component_dir}"):
        os.makedirs(f"{public_dir}/{component_dir}")
    for file in files:
        with open(f"{public_dir}/{component_dir}/{file.filename}", 'wb') as out_file:
            file_path = f"{component_dir}/{file.filename}"
            content = await file.read()  
            out_file.write(content) 
            file = await FileCrud.create(component_id=component_id, path=f"/{file_path}")

    return


@router.delete(
    "/file/{file_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_description="The file has been successfully deleted."
)
async def delete_file(file_id: int):
    """
    Delete a file.
    """
    file = await FileCrud.get(file_id)
    if not file:
        raise not_found
    
    await FileCrud.delete(file_id)

    return
