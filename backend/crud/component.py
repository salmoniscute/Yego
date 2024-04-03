from database.mysql import crud_class_decorator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from models.component import Component as ComponentModel
from schemas import component as ComponentSchema


@crud_class_decorator
class ComponentCrudManager:
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
    
    async def create(self, publisher, newComponent: ComponentSchema.ComponentCreate, db_session: AsyncSession):
        newComponent_dict = newComponent.model_dump()
        component = ComponentModel(publisher=publisher, **newComponent_dict)
        db_session.add(component)
        await db_session.commit()
        db_session.refresh(component)

        return component
    
    async def update(self, component_id: str, updateComponent: ComponentSchema.ComponentUpdate, db_session: AsyncSession):
        updateComponent_dict = updateComponent.model_dump(exclude_none=True)
        if updateComponent_dict:
            stmt = update(ComponentModel).where(ComponentModel.id == component_id).values(updateComponent_dict)
            await db_session.execute(stmt)
            await db_session.commit()

        return 
    
    async def delete(self, component_id: str, db_session: AsyncSession):
        stmt = delete(ComponentModel).where(ComponentModel.id == component_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    