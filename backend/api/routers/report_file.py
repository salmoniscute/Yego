from fastapi import APIRouter, HTTPException, status, Depends
from crud.report_file import ReportFileCrudManager
from schemas import report_file as ReportFileSchema
from .depends import check_report_file_id

ReportFileCrud = ReportFileCrudManager()
router = APIRouter(
    tags=["report_file"],
    prefix="/api"
)

@router.post(
    "/report_file", 
    response_model=ReportFileSchema.ReportFileCreate,
    status_code=201,
    response_description="The report file has been successfully created."
)
async def create_report_file(newReportFile: ReportFileSchema.ReportFileCreate):
    """
    Create a report file with the following information:
    - **file_id**
    - **report_id**
    - **path**
    """
    
    
    report_file = await ReportFileCrud.get_report_file_by_file_id(newReportFile.file_id)
    if report_file:
        raise HTTPException(status_code=409, detail=f"Report file already exists")
    
    # create report file
    report_file = await ReportFileCrud.create_report_file(newReportFile)

    return report_file

@router.get(
    "/report_file/{file_id}", 
    response_description="Get a report file",  
)
async def get_report_file(file_id: str = None):
    print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII\n")
    report_file = await ReportFileCrud.get_report_file_by_file_id(file_id)
    print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\n")
    if report_file:
        return report_file
    raise HTTPException(status_code=404, detail=f"Report file doesn't exist")
    

@router.put(
    "/report_file/{file_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_report_file(newReportFile: ReportFileSchema.ReportFileUpdate, file_id: str = Depends(check_report_file_id)):
    
    
    await ReportFileCrud.update_report_file_by_file_id(file_id, newReportFile)

    return 

@router.delete(
    "/report_file/{file_id}",
    status_code=status.HTTP_204_NO_CONTENT 
)
async def delete_report_file(file_id: str = Depends(check_report_file_id)):

    await ReportFileCrud.delete_report_file_by_file_id(file_id)
    
    return 