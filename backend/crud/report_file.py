from database.mysql import crud_class_decorator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from models.report_file import Report_file as ReportFileModel
from schemas import report_file as ReportFileSchema

@crud_class_decorator
class ReportFileCrudManager:
    async def create_report_file(self, newReportFile: ReportFileSchema.ReportFileCreate, db_session: AsyncSession):
        report_file = ReportFileModel(
            file_id=newReportFile.file_id,
            report_id=newReportFile.report_id,
            path=newReportFile.path
        )
        db_session.add(report_file)
        await db_session.commit()
        db_session.refresh(report_file)

        return report_file

    async def get_report_file_by_file_id(self, file_id: str, db_session: AsyncSession):
        stmt = select(
            ReportFileModel.file_id,
            ReportFileModel.report_id,
            ReportFileModel.path
        ).where(ReportFileModel.file_id == file_id)
        result = await db_session.execute(stmt)
        report_file = result.first()
        if report_file:
            return report_file
        
        return None

    async def update_report_file_by_file_id(self, file_id: str, updateDiscussionTopicFile: ReportFileSchema.ReportFileUpdate, db_session: AsyncSession):
        stmt = update(ReportFileModel).where(ReportFileModel.file_id == file_id).values(
            path=updateDiscussionTopicFile.path
        )
        await db_session.execute(stmt)
        await db_session.commit()

        return 
    
    
    async def delete_report_file_by_file_id(self, file_id: int, db_session: AsyncSession):
        stmt = delete(ReportFileModel).where(ReportFileModel.file_id == file_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    