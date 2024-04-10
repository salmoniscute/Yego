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
    response_model=ReportSchema.ReportCreate,
    status_code=status.HTTP_201_CREATED
)
async def create_report(
    newReport: ReportSchema.ReportCreate,
    uid: str = Depends(check_user_id),
):
    """
    Create a report with the following information:
    - **id**
    - **release_time**
    - **title**
    - **content**
    """
    report = await ReportCrud.get(newReport.id)
    if report:
        raise already_exists
    
    report = await ReportCrud.create(uid, newReport)

    return report

@router.get(
    "/reports",
    response_model=list[ReportSchema.ReportRead]
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
    "/report/{id}", 
    response_model=ReportSchema.ReportRead
)
async def get_report(id: str):
    """ 
    Get a report.
    """
    report = await ReportCrud.get(id)
    if report:
        return report
    
    raise not_found
    

@router.put(
    "/report/{id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_report(
    updateReport: ReportSchema.ReportUpdate,
    id: str = Depends(check_component_id)
):
    """ 
    Update a report with the following information:
    - **title**
    - **content**
    """
    await ReportCrud.update(id, updateReport)

    return 


@router.delete(
    "/report/{id}",
    status_code=status.HTTP_204_NO_CONTENT 
)
async def delete_report(id: str = Depends(check_component_id)):
    """ 
    Delete a report.
    """
    await ReportCrud.delete(id)
    
    return 
