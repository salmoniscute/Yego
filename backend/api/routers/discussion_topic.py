from fastapi import APIRouter, HTTPException, status, Depends

from .depends import check_topic_id, check_user_id, check_discussion_id
from crud.discussion import DiscussionTopicCrudManager
from crud.notification import NotificationCrudManager
from crud.subscription import SubscriptionCrudManager
from crud.selected_course import SelectedCourseCrudManager
from crud.discussion import DiscussionCrudManager
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

NotificationCrud = NotificationCrudManager()
SubscriptionCrud = SubscriptionCrudManager()
SelectedCourseCrud = SelectedCourseCrudManager()
DiscussionCrud = DiscussionCrudManager()
router = APIRouter(
    tags=["Discussion Topic"],
    prefix="/api"
)

@router.post(
    "/discussion_topic", 
    status_code=status.HTTP_201_CREATED
)
async def create_discussion_topic(
    newTopic: DiscussionSchema.DiscussionCreate,
    uid: str = Depends(check_user_id),
    discussion_id: int = Depends(check_discussion_id)
):
    """
    Create a discussion topic with the following information:
    - **release_time**
    - **title**
    - **content**
    """
    topic = await TopicCrud.create(uid, discussion_id, newTopic)
    discussion = await DiscussionCrud.get(discussion_id)
    users = await SelectedCourseCrud.get_by_course_id(discussion["course_id"])
    for user in users:
        if SubscriptionCrud.get(user["uid"], discussion_id):
            await NotificationCrud.create(user["uid"], topic.id, "discussion_topic")
    
    return {"id": topic.id}


@router.get(
    "/discussion_topic/{topic_id}", 
    response_model=DiscussionSchema.DiscussionTopicRead
)
async def get_discussion_topic(
    topic_id: int=Depends(check_topic_id)
):
    """ 
    Get a discussion topic.
    """
    topic = await TopicCrud.get(topic_id)
    if topic:
        return topic
    
    raise not_found


@router.get(
    "/discussion_topics/{discussion_id}",
    response_model=list[DiscussionSchema.DiscussionOfTopics]
)
async def get_discussion_topics_by_discussion_id(
    uid: str = Depends(check_user_id),
    discussion_id: int = Depends(check_discussion_id)
):
    """
    Get all discussion topics by discussion id and the subscription status of user.
    """
    topics = await TopicCrud.get_topics_by_discussion_id(uid, discussion_id)
    if topics:
        return topics
    
    raise not_found
    

@router.put(
    "/discussion_topic/{topic_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_discussion_topic(
    updateDiscussion: DiscussionSchema.DiscussionUpdate,
    topic_id: int = Depends(check_topic_id)
):
    """ 
    Update a discussion topic with the following information:
    - **title**
    - **content**
    """
    await TopicCrud.update(topic_id, updateDiscussion)
    topic = await TopicCrud.get(topic_id)
    discussion = await DiscussionCrud.get(topic["discussion_id"])
    users = await SelectedCourseCrud.get_by_course_id(discussion["course_id"])
    for user in users:
        if SubscriptionCrud.get(user["uid"], topic["id"]) or SubscriptionCrud.get(user["uid"], discussion["id"]):
            await NotificationCrud.create(user["uid"], topic["id"], "discussion_topic")
    
    return 


@router.delete(
    "/discussion_topic/{topic_id}",
    status_code=status.HTTP_204_NO_CONTENT 
)
async def delete_discussion_topic(
    topic_id: int = Depends(check_topic_id)
):
    """ 
    Delete a discussion topic.
    """
    await TopicCrud.delete(topic_id)
    
    return 
