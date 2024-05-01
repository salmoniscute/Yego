from fastapi import APIRouter, HTTPException, status, Depends

from .depends import check_component_id, check_user_id
from crud.discussion import DiscussionTopicReplyCrudManager
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
router = APIRouter(
    tags=["Discussion Topic Reply"],
    prefix="/api"
)

@router.post(
    "/discussion_topic_reply", 
    response_model=DiscussionSchema.DiscussionTopicReplyCreate,
    status_code=status.HTTP_201_CREATED
)
async def create_discussion_topic_reply(
    newReply: DiscussionSchema.DiscussionTopicReplyCreate,
    uid: str = Depends(check_user_id),
    root_id: int = Depends(check_component_id)
):
    """
    Create a discussion topic reply with the following information:
    - **release_time**
    - **title**
    - **content**
    """
    reply = await TopicReplyCrud.create(uid, root_id, newReply)

    return reply

@router.get(
    "/discussion_topic_replies",
    response_model=list[DiscussionSchema.DiscussionTopicReplyRead]
)
async def get_all_discussion_topic_replies():
    """ 
    Get all discussion topic replies.
    """
    replies = await TopicReplyCrud.get_all()
    if replies:
        return replies
    
    raise not_found

@router.get(
    "/discussion_topic_reply/{reply_id}", 
    response_model=DiscussionSchema.DiscussionTopicReplyRead
)
async def get_discussion_topic_reply(
    reply_id: int = Depends(check_component_id)
):
    """ 
    Get a discussion topic reply by its id.
    """
    reply = await TopicReplyCrud.get(reply_id)
    if reply:
        return reply
    
    raise not_found

@router.put(
    "/discussion_topic_reply/{reply_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_discussion_topic_reply(
    updateReply: DiscussionSchema.DiscussionUpdate,
    reply_id: int = Depends(check_component_id)
):
    """ 
    Update a discussion topic reply by its id.
    """
    await TopicReplyCrud.update(reply_id, updateReply)

    return

@router.delete(
    "/discussion_topic_reply/{reply_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_discussion_topic_reply(
    reply_id: int = Depends(check_component_id)
):
    """ 
    Delete a discussion topic reply by its id.
    """
    await TopicReplyCrud.delete(reply_id)

    return