from database.mysql import crud_class_decorator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from models.report import Report as ReportModel
from schemas import report as ReportSchema

@crud_class_decorator
class ReportCrudManager:
    async def create(self, publisher, newReport: ReportSchema.ReportCreate, db_session: AsyncSession):
        newReport_dict = newReport.model_dump()
        report = ReportModel(**newReport_dict, publisher=publisher)
        db_session.add(report)
        await db_session.commit()
        db_session.refresh(report)

        return report

    async def get(self, report_id: str, db_session: AsyncSession):
        stmt = select(ReportModel).where(ReportModel.report_id == report_id)
        result = await db_session.execute(stmt)
        report = result.first()
        
        return report[0] if report else None

    async def get_all(self, db_session: AsyncSession):
        stmt = select(ReportModel)
        result = await db_session.execute(stmt)
        result = result.unique()
        
        return [report[0] for report in result.all()]
    
    async def update(self, report_id: str, updateReport: ReportSchema.ReportUpdate, db_session: AsyncSession):
        updateReport_dict = updateReport.model_dump()
        if updateReport_dict:
            stmt = update(ReportModel).where(ReportModel.report_id == report_id).values(**updateReport_dict)
            await db_session.execute(stmt)
            await db_session.commit()
    
    async def delete(self, report_id: int, db_session: AsyncSession):
        stmt = delete(ReportModel).where(ReportModel.report_id == report_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return