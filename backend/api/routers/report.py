from fastapi import APIRouter, HTTPException, status, Depends
from crud.report import ReportCrudManager
from schemas import report as ReportSchema
from .depends import check_report_id, check_user_id

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
async def create_report(
    newReport: ReportSchema.ReportCreate,
    publisher: str = Depends(check_user_id)
):
    """
    Create a report with the following information:
    - **report_id**
    - **publisher**
    - **title**
    - **release_time**
    - **content**
    """
    
    
    report = await ReportCrud.get(newReport.report_id)
    if report:
        raise HTTPException(status_code=409, detail=f"Report already exists")
    
    # create report
    report = await ReportCrud.create(publisher, newReport)

    return report

@router.get(
  "/report/list",
  response_model=list[ReportSchema.ReportRead],
  response_description="Get all report",  
)
async def get_report_list():
    """ 
    Get all report.
    """
    
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

@router.put(
    "/report/{report_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_report(newReport: ReportSchema.ReportUpdate, report_id: str = Depends(check_report_id)):
    """ 
    Update a report with the following information:
    - **report_id**
    - **publisher**
    - **title**
    - **release_time**
    - **content**
    """
    
    await ReportCrud.update(report_id, newReport)

    return 

@router.delete(
    "/report/{report_id}",
    status_code=status.HTTP_204_NO_CONTENT 
)
async def delete_report(report_id: str = Depends(check_report_id)):
    """ 
    Delete a report.
    """
    
    await ReportCrud.delete(report_id)
    
    return 
  
