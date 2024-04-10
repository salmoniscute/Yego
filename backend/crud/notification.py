from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database.mysql import crud_class_decorator
from models.notification import Notification as NotificationModel
from schemas import notification as NotificationSchema


@crud_class_decorator
class NotificationCrudManager:
    async def create(self, uid: str, component_id: str, newNotification: NotificationSchema.NotificationCreate, db_session: AsyncSession):
        newNotification_dict = newNotification.model_dump()
        notification = NotificationModel(uid=uid, component_id=component_id, **newNotification_dict)
        db_session.add(notification)
        await db_session.commit()

        return notification
     
    async def get(self, uid: str, component_id: str, db_session: AsyncSession):
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
    
    async def update(self, uid: str, component_id: str, updateNotification: NotificationSchema.NotificationUpdate, db_session: AsyncSession):
        updateNotification_dict = updateNotification.model_dump(exclude_none=True)
        if updateNotification_dict:
            stmt = (
                update(NotificationModel)
                .where(NotificationModel.uid == uid)
                .where(NotificationModel.component_id == component_id)
                .values(updateNotification_dict)
            )
            await db_session.execute(stmt)
            await db_session.commit()

        return 
    
    async def delete(self, uid: str, component_id: str, db_session: AsyncSession):
        stmt = (
            delete(NotificationModel)
            .where(NotificationModel.uid == uid)
            .where(NotificationModel.component_id == component_id)
        )
        await db_session.execute(stmt)
        await db_session.commit()

        return
    