from fastapi import APIRouter, HTTPException, status, Depends
from crud.report_reply import ReportReplyCrudManager
from schemas import report_reply as ReportReplySchema
from .depends import check_report_reply_id, check_report_id, check_user_id, check_parent

ReportReplyCrud = ReportReplyCrudManager()
router = APIRouter(
    tags=["report_reply"],
    prefix="/api"
)

@router.post(
    "/report_reply", 
    response_model=ReportReplySchema.ReportReplyCreate,
    status_code=201,
    response_description="The report reply has been successfully created."
)
async def create_report_reply(
    newReportReply: ReportReplySchema.ReportReplyCreate,
    parent: str = None,
    report_id: str = Depends(check_report_id),
    publisher: str = Depends(check_user_id)):
    """
    Create a report with the following information:
    - **reply_id**
    - **parent**
    - **report_id**
    - **publisher**
    - **release_time**
    - **content**
    """
    if parent:
        await ReportReplyCrud.get(parent)    
        if not parent: 
            raise HTTPException(status_code=409, detail=f"parent id do not exisparentt")
    
    report_reply = await ReportReplyCrud.get(newReportReply.reply_id)
    if report_reply:
        raise HTTPException(status_code=409, detail=f"Report reply already exists")
    
    # create report reply
    report_reply = await ReportReplyCrud.create(parent, report_id, publisher, newReportReply)

    return report_reply

@router.get(
    "/report_reply/{reply_id}", 
    response_model=ReportReplySchema.ReportReplyRead,
    response_description="Get a report reply by reply_id",  
)
async def get_report_reply(reply_id: str = None):
    
    report_reply = await ReportReplyCrud.get(reply_id)
    if report_reply:
        return report_reply
    raise HTTPException(status_code=404, detail=f"Report reply doesn't exist")
    

@router.put(
    "/report_reply/{reply_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_report_reply(newReportReply: ReportReplySchema.ReportReplyUpdate, reply_id: str = Depends(check_report_reply_id)):
    
    
    await ReportReplyCrud.update(reply_id, newReportReply)

    return 

@router.delete(
    "/report_reply/{reply_id}",
    status_code=status.HTTP_204_NO_CONTENT 
)
async def delete_report_reply(reply_id: str = Depends(check_report_reply_id)):

    await ReportReplyCrud.delete(reply_id)
    
    return 