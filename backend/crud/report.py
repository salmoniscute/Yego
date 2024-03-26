from database.mysql import crud_class_decorator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from models.report import Report as ReportModel
from schemas import report as ReportSchema

@crud_class_decorator
class ReportCrudManager:
    async def create_report(self, newReport: ReportSchema.ReportCreate, db_session: AsyncSession):
        report = ReportModel(
            report_id=newReport.report_id,
            publisher=newReport.publisher,
            title=newReport.title,
            release_time=newReport.release_time,
            content=newReport.content
        )
        db_session.add(report)
        await db_session.commit()
        db_session.refresh(report)

        return report

    async def get_report_by_report_id(self, report_id: str, db_session: AsyncSession):
        stmt = select(
            ReportModel.report_id,
            ReportModel.publisher,
            ReportModel.title,
            ReportModel.release_time,
            ReportModel.content
        ).where(ReportModel.report_id == report_id)
        result = await db_session.execute(stmt)
        report = result.first()
        if report:
            return report
        
        return None

    async def update_report_by_report_id(self, report_id: str, updateReport: ReportSchema.ReportUpdate, db_session: AsyncSession):
        stmt = update(ReportModel).where(ReportModel.report_id == report_id).values(
            publisher=updateReport.publisher,
            title=updateReport.title,
            release_time=updateReport.release_time,
            content=updateReport.content
        )
        await db_session.execute(stmt)
        await db_session.commit()

        return 
    
    
    async def delete_report_by_report_id(self, report_id: int, db_session: AsyncSession):
        stmt = delete(ReportModel).where(ReportModel.report_id == report_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    
    async def get_all(self, db_session: AsyncSession):
        stmt = select(
            ReportModel.report_id,
            ReportModel.title,
            ReportModel.release_time
        )
        result = await db_session.execute(stmt)
        if result:
            return result
        
        return None