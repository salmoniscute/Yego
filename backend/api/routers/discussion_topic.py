from fastapi import APIRouter, HTTPException, status, Depends
from crud.discussion_topic import DiscussionTopicCrudManager
from schemas import discussion_topic as DiscussionTopicSchema
from .depends import check_discussion_topic_id

DiscussionTopicCrud = DiscussionTopicCrudManager()
router = APIRouter(
    tags=["Discussion Topic"],
    prefix="/api"
)

@router.post(
    "/discussion_topic", 
    response_model=DiscussionTopicSchema.DiscussionTopicCreate,
    status_code=201,
    response_description="The discussion topic has been successfully created."
)
async def create_discussion_topic(newDiscussionTopic: DiscussionTopicSchema.DiscussionTopicCreate):
    """
    Create a discussion topic with the following information:
    - **topic_id**
    - **discussion_id**
    - **publisher**
    - **title**
    - **release_time**
    - **content**
    """
    
    
    discussion_topic = await DiscussionTopicCrud.get_discussion_topic_by_topic_id(newDiscussionTopic.topic_id)
    if discussion_topic:
        raise HTTPException(status_code=409, detail=f"Discussion topic already exists")
    
    # create discussion topic
    discussion_topic = await DiscussionTopicCrud.create_discussion_topic(newDiscussionTopic)

    return discussion_topic

@router.get(
    "/discussion_topic", 
    response_model=DiscussionTopicSchema.DiscussionTopicRead,
    response_description="Get a discussion topic",  
)
async def get_discussion_topic(topic_id: str = None):

    discussion_topic = await DiscussionTopicCrud.get_discussion_topic_by_topic_id(topic_id)
    
    if discussion_topic:
        return discussion_topic
    raise HTTPException(status_code=404, detail=f"Discussion topic doesn't exist")
    

@router.put(
    "/discussion_topic/{topic_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_discussion_topic(newDiscussionTopic: DiscussionTopicSchema.DiscussionTopicUpdate, topic_id: str = Depends(check_discussion_topic_id)):
    
    
    await DiscussionTopicCrud.update_discussion_topic_by_topic_id(topic_id, newDiscussionTopic)

    return 

@router.delete(
    "/discussion_topic/{topic_id}",
    status_code=status.HTTP_204_NO_CONTENT 
)
async def delete_discussion_topic(topic_id: str = Depends(check_discussion_topic_id)):

    await DiscussionTopicCrud.delete_discussion_topic_by_topic_id(topic_id)
    
    return 