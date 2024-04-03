from fastapi import APIRouter, Depends, HTTPException, status

from .depends import check_course_id, check_user_id
from crud.file import FileCrudManager
from schemas import file as FileSchema

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
    owner: str = Depends(check_user_id)
):
    """
    Create a file with the following information:
    """
    
    
    