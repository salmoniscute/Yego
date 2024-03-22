from fastapi import APIRouter, HTTPException, status, Depends
from crud.discussion_topic_file import DiscussionTopicFileCrudManager
from schemas import discussion_topic_file as DiscussionTopicFileSchema
from .depends import check_discussion_topic_file_id
from auth.jwt import create_jwt

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
async def create_discussion_topic_file(newDiscussionTopicFile: DiscussionTopicFileSchema.DiscussionTopicFileCreate):
    """
    Create a discussion topic with the following information:
    - **file_id**
    - **topic_id**
    - **path**
    """
    
    
    discussion_topic_file = await DiscussionTopicFileCrud.get_discussion_topic_file_by_file_id(newDiscussionTopicFile.file_id)
    if discussion_topic_file:
        raise HTTPException(status_code=409, detail=f"Discussion topic already exists")
    
    # create discussion topic file
    discussion_topic_file = await DiscussionTopicFileCrud.create_discussion_topic_file(newDiscussionTopicFile)

    return discussion_topic_file

@router.get(
    "/discussion_topic_file", 
    response_description="Get a discussion topic file",  
)
async def get_discussion_topic_file(file_id: str = None):

    discussion_topic_file = await DiscussionTopicFileCrud.get_discussion_topic_file_by_file_id(file_id)
    
    if discussion_topic_file:
        return create_jwt(discussion_topic_file)
    raise HTTPException(status_code=404, detail=f"Discussion topic file doesn't exist")
    

@router.put(
    "/discussion_topic_file/{file_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_discussion_topic_file(newDiscussionTopicFile: DiscussionTopicFileSchema.DiscussionTopicFileUpdate, file_id: str = Depends(check_discussion_topic_file_id)):
    
    
    await DiscussionTopicFileCrud.update_discussion_topic_file_by_file_id(file_id, newDiscussionTopicFile)

    return 

@router.delete(
    "/discussion_topic_file/{file_id}",
    status_code=status.HTTP_204_NO_CONTENT 
)
async def delete_discussion_topic_file(file_id: str = Depends(check_discussion_topic_file_id)):

    await DiscussionTopicFileCrud.delete_discussion_topic_file_by_file_id(file_id)
    
    return 