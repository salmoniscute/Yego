from datetime import datetime
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database.mysql import crud_class_decorator
from models.base import NotificationType
from models.notification import Notification as NotificationModel
from schemas import notification as NotificationSchema


icon_type = {
    "course_bulletin": "announcement",
    "report": "announcement",
    "course_material": "assignment",
    "course_assignment": "assignment",
    "discussion": "discussion",
    "discussion_topic": "discussion"
}

type_actions = {
    "course_bulletin": {
        "refresh": ["course_bulletin"],
        "course_name": lambda n: f"公告 - {n.component_info.course_bulletin.course_info.name}"
    },
    "report": {
        "refresh": ["report"],
        "course_name": lambda n: "問題回報區"
    },
    "discussion": {
        "refresh": ["discussion"],
        "course_name": lambda n: f"討論區 - {n.component_info.discussion.course_info.name}"
    }
}


@crud_class_decorator
class NotificationCrudManager:
    async def create(self, uid: str, component_id: int, type: NotificationType, newNotification: NotificationSchema.NotificationCreate, db_session: AsyncSession):
        newNotification_dict = newNotification.model_dump()
        notification = NotificationModel(uid=uid, component_id=component_id, release_time=datetime.now().strftime("%Y-%m-%dT%H:%M:%S"), type=type, **newNotification_dict)
        db_session.add(notification)
        await db_session.commit()

        return notification
     
    async def get(self, uid: str, component_id: int, db_session: AsyncSession):
        stmt = (
            select(NotificationModel)
            .where(NotificationModel.uid == uid)
            .where(NotificationModel.component_id == component_id)
        )
        result = await db_session.execute(stmt)
        notification = result.first()

        return notification[0] if notification else None
        
    async def get_all(self, db_session: AsyncSession):
        stmt = select(NotificationModel)
        result = await db_session.execute(stmt)
        result = result.unique()

        return [notification[0] for notification in result.all()]
    
    async def update(self, uid: str, component_id: int, db_session: AsyncSession):
        stmt1 = (
            update(NotificationModel)
            .where(NotificationModel.uid == uid)
            .where(NotificationModel.component_id == component_id)
            .values({"have_read": True})
        )
        await db_session.execute(stmt1)

        stmt2 = select(NotificationModel).where(NotificationModel.uid == uid)
        result = await db_session.execute(stmt2)

        _list = []
        for notification in result:
            action = type_actions[notification[0].type]
            await db_session.refresh(notification[0].component_info, action["refresh"])
            
            _list.append({
                "id": notification[0].id,
                "uid": notification[0].uid,
                "component_id": notification[0].component_id,
                "publisher": notification[0].user_info.name,
                "course_name": action["course_name"](notification[0]),
                "release_time": notification[0].release_time,
                "title": notification[0].component_info.title,
                "content": notification[0].component_info.content,
                "have_read": notification[0].have_read,
                "icon_type": icon_type[notification[0].type]
            })

        await db_session.commit() 

        return _list
    
    async def delete(self, uid: str, component_id: int, db_session: AsyncSession):
        stmt = (
            delete(NotificationModel)
            .where(NotificationModel.uid == uid)
            .where(NotificationModel.component_id == component_id)
        )
        await db_session.execute(stmt)
        await db_session.commit()

        return
    
    async def get_by_uid(self, uid: str, db_session: AsyncSession):
        stmt = select(NotificationModel).where(NotificationModel.uid == uid)
        result = await db_session.execute(stmt)

        _list = []
        for notification in result:
            action = type_actions[notification[0].type]
            await db_session.refresh(notification[0].component_info, action["refresh"])
            
            _list.append({
                "id": notification[0].id,
                "uid": notification[0].uid,
                "component_id": notification[0].component_id,
                "publisher": notification[0].user_info.name,
                "course_name": action["course_name"](notification[0]),
                "release_time": notification[0].release_time,
                "title": notification[0].component_info.title,
                "content": notification[0].component_info.content,
                "have_read": notification[0].have_read,
                "icon_type": icon_type[notification[0].type]
            })

        return _list
    
    async def read_all(self, uid: str, db_session: AsyncSession):
        updateNotification_dict = {"have_read": True}
        stmt1 = (
            update(NotificationModel)
            .where(NotificationModel.uid == uid)
            .values(updateNotification_dict)
        )
        await db_session.execute(stmt1)
        
        stmt2 = select(NotificationModel).where(NotificationModel.uid == uid)
        result = await db_session.execute(stmt2)

        _list = []
        for notification in result:
            action = type_actions[notification[0].type]
            await db_session.refresh(notification[0].component_info, action["refresh"])

            _list.append({
                "id": notification[0].id,
                "uid": notification[0].uid,
                "component_id": notification[0].component_id,
                "publisher": notification[0].user_info.name,
                "course_name": action["course_name"](notification[0]),
                "release_time": notification[0].release_time,
                "title": notification[0].component_info.title,
                "content": notification[0].component_info.content,
                "have_read": notification[0].have_read,
                "icon_type": icon_type[notification[0].type]
            })

        await db_session.commit()

        return _list
    