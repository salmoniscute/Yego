from database.mysql import crud_class_decorator
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from models.subscription import Subscription as SubscriptionModel
from schemas import subscription as SubscriptionSchema


@crud_class_decorator
class SubscriptionCrudManager:
    async def create(self, uid, component_id, newSubscription: SubscriptionSchema.SubscriptionCreate, db_session: AsyncSession):
        newSubscription_dict = newSubscription.model_dump()
        subscription = SubscriptionModel(uid=uid, component_id=component_id, **newSubscription_dict)
        db_session.add(subscription)
        await db_session.commit()

        return subscription
     
    async def get(self, subscription_id: str, db_session: AsyncSession):
        stmt = select(SubscriptionModel).where(SubscriptionModel.id == subscription_id)
        result = await db_session.execute(stmt)
        subscription = result.first()

        return subscription[0] if subscription else None
        
    async def get_all(self, db_session: AsyncSession):
        stmt = select(SubscriptionModel)
        result = await db_session.execute(stmt)
        result = result.unique()

        return [subscription[0] for subscription in result.all()]
    
    async def delete(self, subscription: int, db_session: AsyncSession):
        stmt = delete(SubscriptionModel).where(SubscriptionModel.id == subscription)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    