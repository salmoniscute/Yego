from fastapi import APIRouter, HTTPException, status, Depends

from .depends import check_report_id, check_reply_id, check_user_id
from crud.report_reply import ReportReplyCrudManager
from crud.subscription import SubscriptionCrudManager
from crud.user import UserCrudManager
from crud.notification import NotificationCrudManager
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

SubscriptionCrud = SubscriptionCrudManager()
UserCrud = UserCrudManager()
NotificationCrud = NotificationCrudManager()


@router.post(
    "/report_reply",
    response_model=ReportSchema.ReportReplyReadByID,
    status_code=status.HTTP_201_CREATED
)
async def create_report_reply(
    newReply: ReportSchema.ReportReplyCreate,
    uid: str = Depends(check_user_id),
    root_id: int = Depends(check_report_id),
    parent_id: int = Depends(check_reply_id)
):
    """
    Create a report reply with the following information:
    - **release_time**
    - **content**
    """
    reply = await ReportReplyCrud.create(uid, root_id, parent_id, newReply)
    # reply = await ReportReplyCrud.get(reply.id)
    
    # users = await UserCrud.get_all()
    # for user in users:
    #     if await SubscriptionCrud.get(user.uid, root_id):
    #         await NotificationCrud.create(user.uid, root_id, "report")

    return reply


@router.put(
    "/report_reply/{reply_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_report_reply(
    updateReply: ReportSchema.ReportUpdate,
    reply_id: int = Depends(check_reply_id)
):
    """
    Update a report reply.
    """
    await ReportReplyCrud.update(reply_id, updateReply)

    return


@router.delete(
    "/report_reply/{reply_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_report_reply(reply_id: int):
    """
    Delete a report reply.
    """
    await ReportReplyCrud.delete(reply_id)

    return
