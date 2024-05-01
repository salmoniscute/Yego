from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database.mysql import crud_class_decorator
from models.component import Component as ComponentModel
from models.report import Report as ReportModel
from schemas import report as ReportSchema


@crud_class_decorator
class ReportCrudManager:
    async def create(self, uid: str, newReport: ReportSchema.ReportCreate, db_session: AsyncSession):
        newReport_dict = newReport.model_dump()
        report = ReportModel(**newReport_dict, uid=uid)
        db_session.add(report)
        await db_session.commit()

        return report

    async def get(self, id: str, db_session: AsyncSession):
        stmt = select(ReportModel).where(ReportModel.id == id)
        result = await db_session.execute(stmt)
        report = result.first()
        
        return report[0] if report else None

    async def get_all(self, db_session: AsyncSession):
        stmt = select(ReportModel)
        result = await db_session.execute(stmt)
        result = result.unique()
        
        return [report[0] for report in result.all()]

    async def update(self, id: str, updateReport: ReportSchema.ReportUpdate, db_session: AsyncSession):
        updateReport_dict = updateReport.model_dump(exclude_none=True)
        if updateReport_dict:
            stmt = update(ComponentModel).where(ComponentModel.id == id).values(**updateReport_dict)
            await db_session.execute(stmt)
            await db_session.commit()

        return
    
    async def delete(self, id: int, db_session: AsyncSession):
        stmt = delete(ComponentModel).where(ComponentModel.id == id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
