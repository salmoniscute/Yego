from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database.mysql import crud_class_decorator
from models.subscription import Subscription as SubscriptionModel
from schemas import subscription as SubscriptionSchema


@crud_class_decorator
class SubscriptionCrudManager:
    async def create(self, uid: str, component_id: int, newSubscription: SubscriptionSchema.SubscriptionCreate, db_session: AsyncSession):
        newSubscription_dict = newSubscription.model_dump()
        subscription = SubscriptionModel(uid=uid, component_id=component_id, **newSubscription_dict)
        db_session.add(subscription)
        await db_session.commit()

        return subscription
     
    async def get(self, uid: str, component_id: int, db_session: AsyncSession):
        stmt = (
            select(SubscriptionModel)
            .where(SubscriptionModel.uid == uid)
            .where(SubscriptionModel.component_id == component_id)
        )
        result = await db_session.execute(stmt)
        subscription = result.first()

        return subscription[0] if subscription else None
        
    async def get_all(self, db_session: AsyncSession):
        stmt = select(SubscriptionModel)
        result = await db_session.execute(stmt)
        result = result.unique()

        return [subscription[0] for subscription in result.all()]
    
    async def delete(self, uid: str, component_id: int, db_session: AsyncSession):
        stmt = (
            delete(SubscriptionModel)
            .where(SubscriptionModel.uid == uid)
            .where(SubscriptionModel.component_id == component_id)
        )
        await db_session.execute(stmt)
        await db_session.commit()

        return
    
    async def get_by_uid(self, uid: str, db_session: AsyncSession):
        stmt = (
            select(SubscriptionModel)
            .where(SubscriptionModel.uid == uid)
        )
        result = await db_session.execute(stmt)
        result = result.unique()

        return [subscription[0] for subscription in result.all()]
    
    async def get_by_component_id(self, component_id: int, db_session: AsyncSession):
        stmt = (
            select(SubscriptionModel)
            .where(SubscriptionModel.component_id == component_id)
        )
        result = await db_session.execute(stmt)
        result = result.unique()

        return [subscription[0] for subscription in result.all()]
    