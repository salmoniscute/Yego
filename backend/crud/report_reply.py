from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from crud.component import ComponentCrudManager
from database.mysql import crud_class_decorator
from models.component import Component as ComponentModel
from models.report import Report as ReportModel, ReportReply as ReportReplyModel
from schemas import report as ReportSchema

ComponentCrud = ComponentCrudManager()


@crud_class_decorator
class ReportReplyCrudManager:
    async def create(self, uid: str, root_id: int, parent_id: int, newReportReply: ReportSchema.ReportReplyCreate, db_session: AsyncSession):
        newComponent_dict = newReportReply.model_dump()
        newComponent_dict["title"] = "None"

        # Add Component
        component = await ComponentCrud.create(uid=uid, newComponent=newComponent_dict)

        # Add ReportReply
        reply = ReportReplyModel(id=component.id, root_id=root_id, parent_id=parent_id)
        db_session.add(reply)
        await db_session.commit()

        return reply

    async def get(self, reply_id: int, db_session: AsyncSession):
        stmt = select(ReportReplyModel).where(ReportReplyModel.id == reply_id)
        result = await db_session.execute(stmt)
        reply = result.first()

        obj = {}
        if reply:
            await db_session.refresh(reply[0], ["info"])
            await db_session.refresh(reply[0].info, ["publisher_info"])
            obj = {
                "id": reply[0].id,
                "uid": reply[0].info.publisher_info.uid,
                "publisher": reply[0].info.publisher_info.name,
                "avatar": reply[0].info.publisher_info.avatar,
                "parent_id": reply[0].parent_id,
                "publisher": reply[0].info.publisher_info.name,
                "publisher_avatar": reply[0].info.publisher_info.avatar,
                "release_time": reply[0].info.release_time,
                "content": reply[0].info.content
            }
        
        return obj
    
    async def update(self, reply_id: int, updateReportReply: ReportSchema.ReportUpdate, db_session: AsyncSession):
        updateComponent_dict = updateReportReply.model_dump(exclude_none=True)
        if updateComponent_dict:
            await ComponentCrud.update(reply_id, updateComponent_dict)

        return
    
    async def delete(self, reply_id: int, db_session: AsyncSession):
        stmt = delete(ComponentModel).where(ComponentModel.id == reply_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    