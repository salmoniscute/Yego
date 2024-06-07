from fastapi import APIRouter, HTTPException, status, Depends

from .depends import check_topic_reply_id, check_topic_reply_parnet_id, check_topic_id, check_user_id
from crud.discussion import DiscussionTopicReplyCrudManager, DiscussionTopicCrudManager
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

TopicReplyCrud = DiscussionTopicReplyCrudManager()
DiscussionTopicCrud = DiscussionTopicCrudManager()
NotificationCrud = NotificationCrudManager()
SubscriptionCrud = SubscriptionCrudManager()
SelectedCourseCrud = SelectedCourseCrudManager()
DiscussionCrud = DiscussionCrudManager()
router = APIRouter(
    tags=["Discussion Topic Reply"],
    prefix="/discussion_topic_reply"
)


@router.post(
    "",
    response_model=DiscussionSchema.DiscussionTopicReplyRead,
    status_code=status.HTTP_201_CREATED
)
async def create_discussion_topic_reply(
    newReply: DiscussionSchema.DiscussionTopicReplyCreate,
    uid: str = Depends(check_user_id),
    root_id: int = Depends(check_topic_id),
    parent_id: int = Depends(check_topic_reply_parnet_id)    
):
    """
    Create a discussion topic reply with the following information:
    - **release_time**
    - **title**
    - **content**
    """
    reply = await TopicReplyCrud.create(uid, root_id, parent_id, newReply)
    reply = await TopicReplyCrud.get(reply.id)
    
    topic = await DiscussionTopicCrud.get(root_id)
    discussion = await DiscussionCrud.get(topic["discussion_id"])
    users = await SelectedCourseCrud.get_by_course_id(discussion["course_id"])
    for user in users:
        topic_sub = await SubscriptionCrud.get(user["uid"], root_id)
        discussion_sub = await SubscriptionCrud.get(user["uid"], topic["discussion_id"])
        if topic_sub or discussion_sub:
            await NotificationCrud.create(user["uid"], reply["id"], "discussion_reply", False)
    return reply


@router.put(
    "/{reply_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_discussion_topic_reply(
    updateReply: DiscussionSchema.DiscussionUpdate,
    reply_id: int = Depends(check_topic_reply_id)
):
    """ 
    Update a discussion topic reply by its id.
    """
    await TopicReplyCrud.update(reply_id, updateReply)
    
    reply = await TopicReplyCrud.get(reply_id)
    topic = await DiscussionTopicCrud.get(reply["root_id"])
    discussion = await DiscussionCrud.get(topic["discussion_id"])
    users = await SelectedCourseCrud.get_by_course_id(discussion["course_id"])
    for user in users:
        if SubscriptionCrud.get(user["uid"], reply["root_id"]) or SubscriptionCrud.get(user["uid"], topic["discussion_id"]):
            await NotificationCrud.create(user["uid"], reply["id"], "discussion_reply", True)

    return


@router.delete(
    "/{reply_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_discussion_topic_reply(
    reply_id: int = Depends(check_topic_reply_id)
):
    """ 
    Delete a discussion topic reply by its id.
    """
    await TopicReplyCrud.delete(reply_id)

    return
