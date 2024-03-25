from fastapi import APIRouter, HTTPException, status, Depends
from crud.discussion_reply import DiscussionReplyCrudManager
from schemas import discussion_reply as DiscussionReplySchema
from .depends import check_discussion_reply_id, check_discussion_topic_id, check_user_id

DiscussionReplyCrud = DiscussionReplyCrudManager()
router = APIRouter(
    tags=["Discussion Reply"],
    prefix="/api"
)

@router.post(
    "/discussion_reply", 
    response_model=DiscussionReplySchema.DiscussionReplyCreate,
    status_code=201,
    response_description="The discussion reply has been successfully created."
)
async def create_discussion_reply(
    newDiscussionReply: DiscussionReplySchema.DiscussionReplyCreate,
    topic_id: str = Depends(check_discussion_topic_id),
    publisher: str = Depends(check_user_id)
):
    """
    Create a discussion topic with the following information:
    - **reply_id**
    - **topic_id**
    - **publisher**
    - **release_time**
    - **content**
    - **parent** (optional)
    """
    
    
    discussion_reply = await DiscussionReplyCrud.get(newDiscussionReply.reply_id)
    if discussion_reply:
        raise HTTPException(status_code=409, detail=f"Discussion reply already exists")
    
    # create discussion reply
    discussion_reply = await DiscussionReplyCrud.create(topic_id, publisher, newDiscussionReply)

    return discussion_reply


@router.get(
    "/discussion_replies",
    response_model=list[DiscussionReplySchema.DiscussionReplyRead],
    response_description="Get all discussion replies"
)
async def get_all_discussion_replies():
    """ 
    Get all discussion replies.
    """
    discussion_replies = await DiscussionReplyCrud.get_all()
    if discussion_replies:
        return discussion_replies
    raise HTTPException(status_code=404, detail=f"No discussion replies found")

@router.get(
    "/discussion_reply/{reply_id}", 
    response_model=DiscussionReplySchema.DiscussionReplyRead,
    response_description="Get a discussion reply by reply_id",  
)
async def get_discussion_reply(reply_id: str = None):

    discussion_reply = await DiscussionReplyCrud.get(reply_id)
    
    if discussion_reply:
        return discussion_reply
    raise HTTPException(status_code=404, detail=f"Discussion reply doesn't exist")
    

@router.put(
    "/discussion_reply/{reply_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_discussion_reply(
    newDiscussionReply: DiscussionReplySchema.DiscussionReplyUpdate,
    reply_id: str = Depends(check_discussion_reply_id)
):
    """ 
    Update a discussion reply with the following information:
    - **publisher**
    - **release_time**
    - **content**
    """
    await DiscussionReplyCrud.update(reply_id, newDiscussionReply)
    return 

@router.delete(
    "/discussion_reply/{reply_id}",
    status_code=status.HTTP_204_NO_CONTENT 
)
async def delete_discussion_reply(reply_id: str = Depends(check_discussion_reply_id)):
    """ 
    Delete a discussion reply by reply_id
    """
    await DiscussionReplyCrud.delete(reply_id)
    
    return 