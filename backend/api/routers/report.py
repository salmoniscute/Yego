from fastapi import APIRouter, HTTPException, status, Depends
from crud.report import ReportCrudManager
from schemas import report as ReportSchema
from .depends import check_report_id
from auth.jwt import create_jwt

ReportCrud = ReportCrudManager()
router = APIRouter(
    tags=["report"],
    prefix="/api"
)

@router.post(
    "/report", 
    response_model=ReportSchema.ReportCreate,
    status_code=201,
    response_description="The report has been successfully created."
)
async def create_report(newReport: ReportSchema.ReportCreate):
    """
    Create a report with the following information:
    - **report_id**
    - **publisher**
    - **title**
    - **release_time**
    - **content**
    """
    
    
    report = await ReportCrud.get_report_by_report_id(newReport.report_id)
    if report:
        raise HTTPException(status_code=409, detail=f"Report already exists")
    
    # create report
    report = await ReportCrud.create_report(newReport)

    return report

@router.put(
    "/report/{report_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_report(newReport: ReportSchema.ReportUpdate, report_id: str = Depends(check_report_id)):
    
    
    await ReportCrud.update_report_by_report_id(report_id, newReport)

    return 

@router.delete(
    "/report/{report_id}",
    status_code=status.HTTP_204_NO_CONTENT 
)
async def delete_report(report_id: str = Depends(check_report_id)):

    await ReportCrud.delete_report_by_report_id(report_id)
    
    return 
  
@router.get(
  "/report/list",
  response_model=list[ReportSchema.ReportRead]
)
async def get_report_list():
  
    list = await ReportCrud.get_all()
    result = []
    for report in list:
      result.append({
        "report_id": report.report_id,
        "title": report.title,
        "release_time": report.release_time,
        "reply_number": 1
        })
      
    return result