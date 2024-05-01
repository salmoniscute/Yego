from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database.mysql import crud_class_decorator
from models.component import Component as ComponentModel


@crud_class_decorator
class ComponentCrudManager:
    async def create(self, uid: str, newComponent: dict, db_session: AsyncSession):
        component = ComponentModel(uid=uid, **newComponent)
        db_session.add(component)
        await db_session.commit()

        return component
    
    async def get(self, component_id: str, db_session: AsyncSession):
        stmt = select(ComponentModel).where(ComponentModel.id == component_id)
        result = await db_session.execute(stmt)
        component = result.first()

        return component[0] if component else None
        
    async def get_all(self, db_session: AsyncSession):
        stmt = select(ComponentModel)
        result = await db_session.execute(stmt)
        result = result.unique()

        return [component[0] for component in result.all()]
    
    async def update(self, component_id: str, updateComponent: dict, db_session: AsyncSession):
        if updateComponent:
            stmt = update(ComponentModel).where(ComponentModel.id == component_id).values(updateComponent)
            await db_session.execute(stmt)
            await db_session.commit()

        return 
    
    async def delete(self, component_id: str, db_session: AsyncSession):
        stmt = delete(ComponentModel).where(ComponentModel.id == component_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    