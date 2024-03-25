from fastapi import APIRouter, HTTPException, status, Depends
from crud.course_bulletin_file import CourseBulletinFileCrudManager
from schemas import course_bulletin_file as CourseBulletinFileSchema
from .depends import check_course_bulletin_id, check_course_bulletin_file_id

CourseBulletinFileCrud = CourseBulletinFileCrudManager()
router = APIRouter(
    tags=["Course Bulletin File"],
    prefix="/api"
)

@router.post(
    "/course_bulletin_file", 
    response_model=CourseBulletinFileSchema.CourseBulletinFileCreate,
    status_code=201,
    response_description="The bulletin file has been successfully created."
)
async def create_course_bulletin_file(
    newCourseBulletinFile: CourseBulletinFileSchema.CourseBulletinFileCreate,
    cb_id: str = Depends(check_course_bulletin_id)
):
    """
    Create a bulletin file with the following information:
    - **file_id**
    - **path**
    - **cb_id** ( should be existed )
    """
    
    
    course_bulletin_file = await CourseBulletinFileCrud.get(newCourseBulletinFile.file_id)
    if course_bulletin_file:
        raise HTTPException(status_code=409, detail=f"Bulletin file already exists")
    
    # create bulletin file
    course_bulletin_file = await CourseBulletinFileCrud.create(cb_id, newCourseBulletinFile)

    return course_bulletin_file


@router.get(
    "/course_bulletin_files",
    response_model=list[CourseBulletinFileSchema.CourseBulletinFileRead],
    response_description="Get all bulletin files"
)
async def get_all_course_bulletin_files():
    """ 
    Get all course bulletin files.
    """
    course_bulletin_files = await CourseBulletinFileCrud.get_all()
    if course_bulletin_files:
        return course_bulletin_files
    raise HTTPException(status_code=404, detail=f"No bulletin files found")

@router.get(
    "/course_bulletin_file/{file_id}", 
    response_model=CourseBulletinFileSchema.CourseBulletinFileRead,
    response_description="Get a course bulletin file",  
)
async def get_course_bulletin_file(file_id: str):
    """ 
    Get a course bulletin file.
    """
    course_bulletin_file = await CourseBulletinFileCrud.get(file_id)
    
    if course_bulletin_file:
        return course_bulletin_file
    raise HTTPException(status_code=404, detail=f"Bulletin file doesn't exist")
    

@router.put(
    "/course_bulletin_file/{file_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_course_bulletin_file(
    updateCourseBulletinFile: CourseBulletinFileSchema.CourseBulletinFileUpdate,
    file_id: str = Depends(check_course_bulletin_file_id)
):
    """ 
    Update a course bulletin file.
    - **path**
    """
    await CourseBulletinFileCrud.update(file_id, updateCourseBulletinFile)
    return 

@router.delete(
    "/course_bulletin_file/{file_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_course_bulletin_file(file_id: str = Depends(check_course_bulletin_file_id)):
    """ 
    Delete a course bulletin.
    """
    await CourseBulletinFileCrud.delete(file_id)
    
    return 