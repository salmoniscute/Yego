from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database.mysql import crud_class_decorator
from models.group import Group as GroupModel
from schemas import group as GroupSchema


@crud_class_decorator
class GroupCrudManager:
    async def create(self, course_id: int, newGroup: GroupSchema.GroupCreate, db_session: AsyncSession):
        newGroup_dict = newGroup.model_dump()
        group = GroupModel(course_id, **newGroup_dict)
        db_session.add(group)
        await db_session.commit()

        return group
    
    async def get(self, group_id: int, db_session: AsyncSession):
        stmt = select(GroupModel).where(GroupModel.id == group_id)
        result = await db_session.execute(stmt)
        group = result.first()

        return group[0] if group else None
        
    async def get_all(self, db_session: AsyncSession):
        stmt = select(GroupModel)
        result = await db_session.execute(stmt)
        result = result.unique()

        return [group[0] for group in result.all()]
    
    async def update(self, group_id: int, updateGroup: GroupSchema.GroupUpdate, db_session: AsyncSession):
        updateGroup_dict = updateGroup.model_dump(exclude_none=True)
        if updateGroup_dict:
            stmt = update(GroupModel).where(GroupModel.id == group_id).values(updateGroup_dict)
            await db_session.execute(stmt)
            await db_session.commit()

        return 
    
    async def delete(self, group_id: int, db_session: AsyncSession):
        stmt = delete(GroupModel).where(GroupModel.id == group_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    