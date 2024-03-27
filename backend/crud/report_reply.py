from database.mysql import crud_class_decorator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from models.report_reply import ReportReply as ReportReplyModel
from schemas import report_reply as ReportReplySchema

@crud_class_decorator
class ReportReplyCrudManager:
    async def create_report_reply(self, newReportReply: ReportReplySchema.ReportReplyCreate, db_session: AsyncSession):
        report_reply = ReportReplyModel(
            reply_id=newReportReply.reply_id,
            parent=newReportReply.parent,
            report_id=newReportReply.report_id,
            publisher=newReportReply.publisher,
            release_time=newReportReply.release_time,
            content=newReportReply.content
        )
        db_session.add(report_reply)
        await db_session.commit()
        db_session.refresh(report_reply)

        return report_reply

    async def get_report_reply_by_reply_id(self, reply_id: str, db_session: AsyncSession):
        stmt = select(
            ReportReplyModel.reply_id,
            ReportReplyModel.parent,
            ReportReplyModel.report_id,
            ReportReplyModel.publisher,
            ReportReplyModel.release_time,
            ReportReplyModel.content
        ).where(ReportReplyModel.reply_id == reply_id)
        result = await db_session.execute(stmt)
        report_reply = result.first()
        if report_reply:
            return report_reply
        
        return None

    async def update_report_reply_by_reply_id(self, reply_id: str, updateReportReply: ReportReplySchema.ReportReplyUpdate, db_session: AsyncSession):
        stmt = update(ReportReplyModel).where(ReportReplyModel.reply_id == reply_id).values(
            publisher=updateReportReply.publisher,
            release_time=updateReportReply.release_time,
            content=updateReportReply.content   
        )
        await db_session.execute(stmt)
        await db_session.commit()

        return 
    
    
    async def delete_report_reply_by_reply_id(self, reply_id: int, db_session: AsyncSession):
        stmt = delete(ReportReplyModel).where(ReportReplyModel.reply_id == reply_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    