from fastapi import APIRouter, HTTPException, status, Depends

from .depends import check_report_id, check_user_id
from crud.report import ReportCrudManager
from crud.subscription import SubscriptionCrudManager
from crud.notification import NotificationCrudManager
from crud.user import UserCrudManager
from schemas import report as ReportSchema

not_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, 
    detail="Report does not exist"
)

already_exists = HTTPException(
    status_code=status.HTTP_409_CONFLICT, 
    detail="Report already exists"
)

ReportCrud = ReportCrudManager()
router = APIRouter(
    tags=["Report"],
    prefix="/api"
)

SubscriptionCrud = SubscriptionCrudManager()
NotificationCrud = NotificationCrudManager()
UserCrud = UserCrudManager()


@router.post(
    "/report", 
    status_code=status.HTTP_201_CREATED
)
async def create_report(
    newReport: ReportSchema.ReportCreate,
    uid: str = Depends(check_user_id)
):
    """
    Create a report with the following information:
    - **title**
    - **content**
    """    
    report = await ReportCrud.create(uid, newReport)
    return {"id": report.id}


@router.get(
    "/reports",
    response_model=list[ReportSchema.ReportListRead]
)
async def get_all_reports():
    """ 
    Get all reports.
    """
    reports = await ReportCrud.get_all()
    if reports:
        return reports
    
    raise not_found


@router.get(
    "/report/{report_id}", 
    response_model=ReportSchema.ReportReadByID
)
async def get_report(
    report_id: int = Depends(check_report_id)
):
    """ 
    Get a report.
    """
    report = await ReportCrud.get(report_id)
    if report:
        return report
    
    raise not_found
    

@router.put(
    "/report/{report_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_report(
    updateReport: ReportSchema.ReportUpdate,
    report_id: int = Depends(check_report_id)
):
    """ 
    Update a report with the following information:
    - **title**
    - **content**
    """
    await ReportCrud.update(report_id, updateReport)
    
    # users = await UserCrud.get_all()
    # for user in users:
    #     if await SubscriptionCrud.get(user.uid, report_id):
    #         await NotificationCrud.create(user.uid, report_id, "report")
    

    return 


@router.delete(
    "/report/{report_id}",
    status_code=status.HTTP_204_NO_CONTENT 
)
async def delete_report(report_id: int = Depends(check_report_id)):
    """ 
    Delete a report.
    """
    await ReportCrud.delete(report_id)
    
    return 
