from database.mysql import crud_class_decorator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from models.report_file import ReportFile as ReportFileModel
from schemas import report_file as ReportFileSchema

@crud_class_decorator
class ReportFileCrudManager:
    async def create(self, report_id, newReportFile: ReportFileSchema.ReportFileCreate, db_session: AsyncSession):
        newReportFile_dict = newReportFile.model_dump()
        report_file = ReportFileModel(**newReportFile_dict, report_id=report_id)
        db_session.add(report_file)
        await db_session.commit()
        db_session.refresh(report_file)

        return report_file

    async def get(self, file_id: str, db_session: AsyncSession):
        stmt = select(ReportFileModel).where(ReportFileModel.file_id == file_id)
        result = await db_session.execute(stmt)
        report_file = result.first()
        
        return report_file[0] if report_file else None
    
    async def get_all(self, db_session: AsyncSession):
        stmt = select(ReportFileModel)
        result = await db_session.execute(stmt)
        result = result.unique()
        
        return [report_file[0] for report_file in result.all()]

    async def update(self, file_id: str, updateReportFile: ReportFileSchema.ReportFileUpdate, db_session: AsyncSession):
        updateReportFile_dict = updateReportFile.model_dump()
        if updateReportFile_dict:
            stmt = update(ReportFileModel).where(ReportFileModel.file_id == file_id).values(**updateReportFile_dict)
            await db_session.execute(stmt)
            await db_session.commit()
    
    async def delete(self, file_id: int, db_session: AsyncSession):
        stmt = delete(ReportFileModel).where(ReportFileModel.file_id == file_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    