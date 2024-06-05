from fastapi import APIRouter, Depends, HTTPException, status, UploadFile
from fastapi.responses import FileResponse
from aiofiles import open as async_open

from asyncio import gather, create_task
from os import makedirs
from os.path import isdir, isfile

from crud.file import FileCrudManager
from schemas import file as FileSchema

from .depends import check_component_id

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
    prefix="/file"
)

@router.get(
    "",
    status_code=status.HTTP_200_OK
)
async def get_file(
    file_id: str
):
    file = await FileCrud.get(file_id)
    if not file:
        raise not_found
    
    path = file.path
    if not isfile(path):
        raise not_found
    
    return FileResponse(path)


@router.post(
    "",
    status_code=status.HTTP_204_NO_CONTENT,
    response_description="The file has been successfully created."
)
async def create_files(
    files: list[UploadFile],
    component_id: int = Depends(check_component_id)
):
    target_directory = f"data/component/{component_id}"
    if not isdir(target_directory):
        makedirs(target_directory)

    async def func(file: UploadFile):
        target_path = f"{target_directory}/{file.filename}"
        async with async_open(target_path, "wb") as output:
            await output.write(await file.read())
            await FileCrud.create(component_id=component_id, path=target_path)
    tasks = [
        create_task(func(file)) for file in files
    ]
    await gather(*tasks)

    return


@router.delete(
    "/{file_id}",
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
