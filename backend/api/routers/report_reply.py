from fastapi import APIRouter, HTTPException, status, Depends

from .depends import check_component_id, check_user_id
from crud.report import ReportReplyCrudManager
from schemas import report as ReportSchema

not_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, 
    detail="Report does not exist"
)

already_exists = HTTPException(
    status_code=status.HTTP_409_CONFLICT, 
    detail="Report already exists"
)

ReportReplyCrud = ReportReplyCrudManager()
router = APIRouter(
    tags=["Report Reply"],
    prefix="/api"
)

@router.post(
    "/report_reply", 
    response_model=ReportSchema.ReportReplyCreate,
    status_code=status.HTTP_201_CREATED
)
async def create_report_reply(
    newReply: ReportSchema.ReportReplyCreate,
    uid: str = Depends(check_user_id),
    root_id: int = Depends(check_component_id)
):
    """
    Create a report reply with the following information:
    - **release_time**
    - **title**
    - **content**
    """
    reply = await ReportReplyCrud.create(uid, root_id, newReply)

    return reply

@router.get(
    "/report_replies",
    response_model=list[ReportSchema.ReportReplyRead],
    deprecated=True
)
async def get_all_report_replies():
    """ 
    Get all report replies.
    """
    replies = await ReportReplyCrud.get_all()
    if replies:
        return replies  
    
    raise not_found

@router.get(
    "/report_reply/{reply_id}", 
    response_model=ReportSchema.ReportReplyRead
)
async def get_report_reply(reply_id: int):
    """
    Get a report reply by its id.
    """
    reply = await ReportReplyCrud.get(reply_id)
    if reply:
        return reply
    
    raise not_found

@router.put(
    "/report_reply/{reply_id}",
    response_model=ReportSchema.ReportReplyRead
)
async def update_report_reply(
    updateReply: ReportSchema.ReportUpdate,
    reply_id: int = Depends(check_component_id)
):
    """
    Update a report reply by its id.
    """
    reply = await ReportReplyCrud.update(reply_id, updateReply)

    return reply

@router.delete(
    "/report_reply/{reply_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_report_reply(reply_id: int):
    """
    Delete a report reply by its id.
    """
    await ReportReplyCrud.delete(reply_id)

    return