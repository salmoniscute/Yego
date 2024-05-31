from datetime import datetime
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database.mysql import crud_class_decorator
from models.base import NotificationType
from models.course_material import CourseMaterial as CourseMaterialModel
from models.discussion import Discussion as DiscussionModel, DiscussionTopic as DiscussionTopicModel
from models.notification import Notification as NotificationModel

icon_type = {
    "course_bulletin": "announcement",
    "material_info": "assignment",
    "discussion": "discussion",
    "discussion_topic": "discussion",
    "discussion_reply": "discussion"
}

type_actions = {
    "course_bulletin": {
        "refresh": ["course_bulletin"],
        "course_name": "公告 - "
    },
    "discussion": {
        "refresh": ["discussion"],
        "course_name": "討論區 - "
    },
    "discussion_topic": {
        "refresh": ["topic"],
        "course_name": "討論主題 - "
    },
    "discussion_reply": {
        "refresh": ["discussion_reply"],
        "course_name": "討論回覆 - "
    },
    "material_info": {
        "refresh": ["material_info"],
        "course_name": "課程教材 - "
    }
    
}
    

@crud_class_decorator
class NotificationCrudManager:
    async def create(self, uid: str, component_id: int, type: NotificationType, db_session: AsyncSession):
        notification = NotificationModel(uid=uid, component_id=component_id, release_time=datetime.now().strftime("%Y-%m-%dT%H:%M:%S"), type=type, have_read=False)
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
                "course_name": action["course_name"],
                "release_time": notification[0].release_time,
                "title": notification[0].component_info.title,
                "content": notification[0].component_info.content,
                "have_read": notification[0].have_read,
                "icon_type": icon_type[notification[0].type]
            })

            if notification[0].type == "course_bulletin":
                _list[-1]["course_name"] += notification[0].component_info.course_bulletin.course_info.name
            elif notification[0].type == "discussion":
                _list[-1]["course_name"] += notification[0].component_info.discussion.course_info.name
            elif notification[0].type == "discussion_topic":
                stmt = select(DiscussionModel).where(DiscussionModel.id == notification[0].component_info.topic.discussion_id)
                result = await db_session.execute(stmt)
                discussion = result.first()
                _list[-1]["course_name"] += discussion[0].course_info.name
            elif notification[0].type == "discussion_reply":
                stmt = select(DiscussionTopicModel).where(DiscussionTopicModel.id == notification[0].component_info.discussion_reply.root_id)
                result = await db_session.execute(stmt)
                topic = result.first()
                stmt = select(DiscussionModel).where(DiscussionModel.id == topic[0].discussion_id)
                result = await db_session.execute(stmt)
                discussion = result.first()
                _list[-1]["course_name"] += discussion[0].course_info.name
            elif notification[0].type == "material_info":
                stmt = select(CourseMaterialModel).where(CourseMaterialModel.id == notification[0].component_info.material_info.material_id)
                result = await db_session.execute(stmt)
                course_material = result.first()
                _list[-1]["course_name"] += course_material[0].course_info.name

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
                "course_name": action["course_name"],
                "release_time": notification[0].release_time,
                "title": notification[0].component_info.title,
                "content": notification[0].component_info.content,
                "have_read": notification[0].have_read,
                "icon_type": icon_type[notification[0].type]
            })

            if notification[0].type == "course_bulletin":
                _list[-1]["course_name"] += notification[0].component_info.course_bulletin.course_info.name
            elif notification[0].type == "discussion":
                _list[-1]["course_name"] += notification[0].component_info.discussion.course_info.name
            elif notification[0].type == "discussion_topic":
                stmt = select(DiscussionModel).where(DiscussionModel.id == notification[0].component_info.topic.discussion_id)
                result = await db_session.execute(stmt)
                discussion = result.first()
                _list[-1]["course_name"] += discussion[0].course_info.name
            elif notification[0].type == "discussion_reply":
                stmt = select(DiscussionTopicModel).where(DiscussionTopicModel.id == notification[0].component_info.discussion_reply.root_id)
                result = await db_session.execute(stmt)
                topic = result.first()
                stmt = select(DiscussionModel).where(DiscussionModel.id == topic[0].discussion_id)
                result = await db_session.execute(stmt)
                discussion = result.first()
                _list[-1]["course_name"] += discussion[0].course_info.name
            elif notification[0].type == "material_info":
                stmt = select(CourseMaterialModel).where(CourseMaterialModel.id == notification[0].component_info.material_info.material_id)
                result = await db_session.execute(stmt)
                course_material = result.first()
                _list[-1]["course_name"] += course_material[0].course_info.name

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
                "course_name": action["course_name"],
                "release_time": notification[0].release_time,
                "title": notification[0].component_info.title,
                "content": notification[0].component_info.content,
                "have_read": notification[0].have_read,
                "icon_type": icon_type[notification[0].type]
            })

            if notification[0].type == "course_bulletin":
                _list[-1]["course_name"] += notification[0].component_info.course_bulletin.course_info.name
            elif notification[0].type == "discussion":
                _list[-1]["course_name"] += notification[0].component_info.discussion.course_info.name
            elif notification[0].type == "discussion_topic":
                stmt = select(DiscussionModel).where(DiscussionModel.id == notification[0].component_info.topic.discussion_id)
                result = await db_session.execute(stmt)
                discussion = result.first()
                _list[-1]["course_name"] += discussion[0].course_info.name
            elif notification[0].type == "discussion_reply":
                stmt = select(DiscussionTopicModel).where(DiscussionTopicModel.id == notification[0].component_info.discussion_reply.root_id)
                result = await db_session.execute(stmt)
                topic = result.first()
                stmt = select(DiscussionModel).where(DiscussionModel.id == topic[0].discussion_id)
                result = await db_session.execute(stmt)
                discussion = result.first()
                _list[-1]["course_name"] += discussion[0].course_info.name
            elif notification[0].type == "material_info":
                stmt = select(CourseMaterialModel).where(CourseMaterialModel.id == notification[0].component_info.material_info.material_id)
                result = await db_session.execute(stmt)
                course_material = result.first()
                _list[-1]["course_name"] += course_material[0].course_info.name

        await db_session.commit()

        return _list
    