from fastapi import APIRouter, Depends, HTTPException, status

from .depends import check_component_id, check_user_id
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
    response_model=FileSchema.FileCreate,
    status_code=status.HTTP_201_CREATED,
    response_description="The file has been successfully created."
)
async def create_file(
    newFile: FileSchema.FileCreate,
    owner: str = Depends(check_user_id),
    component_id: str = Depends(check_component_id)
):
    """
    Create a file with the following information:
    - **id**
    - **owner**
    - **component_id**
    - **path**
    """
    file = await FileCrud.get(newFile.id)
    if file:
        raise already_exists
    
    # create file
    file = await FileCrud.create(owner=owner, component_id=component_id, newFile=newFile)

    return file
    
    