from fastapi import APIRouter, HTTPException, status, Depends

from .depends import check_component_id, check_user_id
from crud.report import ReportCrudManager
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


@router.post(
    "/report", 
    status_code=status.HTTP_204_NO_CONTENT
)
async def create_report(
    newReport: ReportSchema.ReportCreate,
    uid: str = Depends(check_user_id)
):
    """
    Create a report with the following information:
    - **release_time**
    - **title**
    - **content**
    """    
    report = await ReportCrud.create(uid, newReport)

    return report

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
    report_id: int = Depends(check_component_id)
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
    report_id: int = Depends(check_component_id)
):
    """ 
    Update a report with the following information:
    - **title**
    - **content**
    """
    await ReportCrud.update(report_id, updateReport)

    return 


@router.delete(
    "/report/{report_id}",
    status_code=status.HTTP_204_NO_CONTENT 
)
async def delete_report(report_id: int = Depends(check_component_id)):
    """ 
    Delete a report.
    """
    await ReportCrud.delete(report_id)
    
    return 
