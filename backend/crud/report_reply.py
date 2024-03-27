from database.mysql import crud_class_decorator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from models.report_reply import ReportReply as ReportReplyModel
from schemas import report_reply as ReportReplySchema

@crud_class_decorator
class ReportReplyCrudManager:
    async def create(self, parent, report_id, publisher, newReportReply: ReportReplySchema.ReportReplyCreate, db_session: AsyncSession):
        newReportReply_dict = newReportReply.model_dump()
        report_reply = ReportReplyModel(**newReportReply_dict, parent=parent, report_id=report_id, publisher=publisher)
        db_session.add(report_reply)
        await db_session.commit()
        db_session.refresh(report_reply)

        return report_reply

    async def get(self, reply_id: str, db_session: AsyncSession):
        stmt = select(ReportReplyModel).where(ReportReplyModel.reply_id == reply_id)
        result = await db_session.execute(stmt)
        report_reply = result.first()
        
        return report_reply[0] if report_reply else None


    async def update(self, reply_id: str, updateReportReply: ReportReplySchema.ReportReplyUpdate, db_session: AsyncSession):
        updateReportReply_dict = updateReportReply.model_dump()
        if updateReportReply_dict:
            stmt = update(ReportReplyModel).where(ReportReplyModel.reply_id == reply_id).values(**updateReportReply_dict)
            await db_session.execute(stmt)
            await db_session.commit()

        return 
    
    
    async def delete(self, reply_id: int, db_session: AsyncSession):
        stmt = delete(ReportReplyModel).where(ReportReplyModel.reply_id == reply_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    