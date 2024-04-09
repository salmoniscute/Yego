from fastapi import APIRouter, HTTPException, status, Depends

from .depends import check_component_id, check_course_id, check_user_id
from crud.discussion import DiscussionTopicCrudManager
from schemas import discussion as DiscussionSchema

not_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, 
    detail="Discussion Topic does not exist"
)

already_exists = HTTPException(
    status_code=status.HTTP_409_CONFLICT, 
    detail="Discussion Topic already exists"
)

TopicCrud = DiscussionTopicCrudManager()
router = APIRouter(
    tags=["Discussion Topic"],
    prefix="/api"
)

@router.post(
    "/discussion_topic", 
    response_model=DiscussionSchema.DiscussionCreate,
    status_code=status.HTTP_201_CREATED
)
async def create_discussion_topic(
    newTopic: DiscussionSchema.DiscussionCreate,
    uid: str = Depends(check_user_id),
    discussion_id: str = Depends(check_course_id)
):
    """
    Create a discussion topic with the following information:
    - **id**
    - **release_time**
    - **title**
    - **content**
    """
    topic = await TopicCrud.get(newTopic.id)
    if topic:
        raise already_exists
    
    topic = await TopicCrud.create(uid, discussion_id, newTopic)

    return topic


@router.get(
    "/discussion_topics",
    response_model=list[DiscussionSchema.DiscussionTopicRead]
)
async def get_all_discussion_topics():
    """ 
    Get all discussion topics.
    """
    topics = await TopicCrud.get_all()
    if topics:
        return topics
    
    raise not_found


@router.get(
    "/discussion_topic/{topic_id}", 
    response_model=DiscussionSchema.DiscussionRead
)
async def get_discussion_topic(topic_id: str):
    """ 
    Get a discussion topic.
    """
    topic = await TopicCrud.get(topic_id)
    if topic:
        return topic
    
    raise not_found
    

@router.put(
    "/discussion_topic/{topic_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_discussion_topic(
    updateDiscussion: DiscussionSchema.DiscussionUpdate,
    topic_id: str = Depends(check_component_id)
):
    """ 
    Update a discussion topic with the following information:
    - **title**
    - **content**
    """
    await TopicCrud.update(topic_id, updateDiscussion)

    return 


@router.delete(
    "/discussion_topic/{topic_id}",
    status_code=status.HTTP_204_NO_CONTENT 
)
async def delete_discussion_topic(topic_id: str = Depends(check_component_id)):
    """ 
    Delete a discussion topic.
    """
    await TopicCrud.delete(topic_id)
    
    return 
