from fastapi import APIRouter, HTTPException, status, Depends
from crud.discussion_topic_file import DiscussionTopicFileCrudManager
from schemas import discussion_topic_file as DiscussionTopicFileSchema
from .depends import check_discussion_topic_file_id, check_discussion_topic_id

DiscussionTopicFileCrud = DiscussionTopicFileCrudManager()
router = APIRouter(
    tags=["Discussion Topic File"],
    prefix="/api"
)

@router.post(
    "/discussion_topic_file", 
    response_model=DiscussionTopicFileSchema.DiscussionTopicFileCreate,
    status_code=201,
    response_description="The discussion topic file has been successfully created."
)
async def create_discussion_topic_file(
    newDiscussionTopicFile: DiscussionTopicFileSchema.DiscussionTopicFileCreate,
    topic_id: str = Depends(check_discussion_topic_id)
):
    """
    Create a discussion topic with the following information:
    - **file_id**
    - **topic_id**
    - **path**
    """
    
    
    discussion_topic_file = await DiscussionTopicFileCrud.get(newDiscussionTopicFile.file_id)
    if discussion_topic_file:
        raise HTTPException(status_code=409, detail=f"Discussion topic already exists")
    
    # create discussion topic file
    discussion_topic_file = await DiscussionTopicFileCrud.create(topic_id, newDiscussionTopicFile)

    return discussion_topic_file


@router.get(
    "/discussion_topic_files",
    response_model=list[DiscussionTopicFileSchema.DiscussionTopicFileRead],
    response_description="Get all discussion topic files"
)
async def get_all_discussion_topic_files():
    """ 
    Get all discussion topic files.
    """
    discussion_topic_files = await DiscussionTopicFileCrud.get_all()
    if discussion_topic_files:
        return discussion_topic_files
    raise HTTPException(status_code=404, detail=f"No discussion topic files found")

@router.get(
    "/discussion_topic_file/{file_id}", 
    response_model=DiscussionTopicFileSchema.DiscussionTopicFileRead,
    response_description="Get a discussion topic file",  
)
async def get_discussion_topic_file(file_id: str = None):
    """ 
    Get a discussion topic file by file_id.
    """
    discussion_topic_file = await DiscussionTopicFileCrud.get(file_id)
    
    if discussion_topic_file:
        return discussion_topic_file
    raise HTTPException(status_code=404, detail=f"Discussion topic file doesn't exist")
    

@router.put(
    "/discussion_topic_file/{file_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_discussion_topic_file(
    newDiscussionTopicFile: DiscussionTopicFileSchema.DiscussionTopicFileUpdate,
    file_id: str = Depends(check_discussion_topic_file_id)
):
    """
    Update a discussion topic file with the following information:
    - **file_id**
    - **topic_id**
    - **path**
    """    
    await DiscussionTopicFileCrud.update(file_id, newDiscussionTopicFile)
    return 

@router.delete(
    "/discussion_topic_file/{file_id}",
    status_code=status.HTTP_204_NO_CONTENT 
)
async def delete_discussion_topic_file(file_id: str = Depends(check_discussion_topic_file_id)):
    """
    Delete a discussion topic file by file_id
    """
    await DiscussionTopicFileCrud.delete(file_id)
    
    return 