from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from crud.component import ComponentCrudManager
from database.mysql import crud_class_decorator
from models.component import Component as ComponentModel
from models.report import Report as ReportModel, ReportReply as ReportReplyModel
from schemas import report as ReportSchema

ComponentCrud = ComponentCrudManager()


@crud_class_decorator
class ReportCrudManager:
    async def create(self, uid: str, newReport: ReportSchema.ReportCreate, db_session: AsyncSession):
        newComponent_dict = newReport.model_dump()

        # Add Component
        component = await ComponentCrud.create(uid, newComponent_dict)

        # Add Report
        report = ReportModel(id=component.id)
        db_session.add(report)
        await db_session.commit()

        return report

    async def get(self, report_id: int, db_session: AsyncSession):
        stmt = select(ReportModel).where(ReportModel.id == report_id)
        result = await db_session.execute(stmt)
        report = result.first()
    
        obj = {}
        if report:
            await db_session.refresh(report[0], ["info"])

            obj = {
                "id": report[0].id,
                "publisher": report[0].info.publisher_info.name,
                "publisher_avatar": report[0].info.publisher_info.avatar,
                "release_time": report[0].info.release_time,
                "title": report[0].info.title,
                "content": report[0].info.content,
                "files": report[0].info.files,
                "replies": []
            }

            stmt = select(ReportReplyModel).where(ReportReplyModel.root_id == report[0].id)
            replies = await db_session.execute(stmt)

            for reply in replies:
                await db_session.refresh(reply[0], ["info"])
                obj["replies"].append({
                    "id": reply[0].id,
                    "uid": reply[0].info.publisher_info.uid,
                    "parent_id": reply[0].parent_id,
                    "publisher": reply[0].info.publisher_info.name,
                    "publisher_avatar": reply[0].info.publisher_info.avatar,
                    "release_time": reply[0].info.release_time,
                    "content": reply[0].info.content
                })

        return obj
    
    async def get_all(self, db_session: AsyncSession):
        stmt = select(ReportModel)
        result = await db_session.execute(stmt)
        
        _list = []
        for report in result:
            await db_session.refresh(report[0], ["info"])
            stmt = select(ReportReplyModel).where(ReportReplyModel.root_id == report[0].id)
            record = await db_session.execute(stmt)

            _list.append({
                "id": report[0].id,
                "release_time": report[0].info.release_time,
                "title": report[0].info.title,
                "reply_number": len(record.all())
            })
        
        return _list

    async def update(self, report_id: int, updateReport: ReportSchema.ReportUpdate, db_session: AsyncSession):
        updateComponent_dict = updateReport.model_dump(exclude_none=True)
        if updateComponent_dict:
            await ComponentCrud.update(report_id, updateComponent_dict)

        return
    
    async def delete(self, report_id: int, db_session: AsyncSession):
        stmt = delete(ComponentModel).where(ComponentModel.id == report_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
