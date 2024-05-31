from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database.mysql import crud_class_decorator
from models.group import Group as GroupModel
from models.selected_course import SelectedCourse as SelectedCourseModel
from schemas import group as GroupSchema


@crud_class_decorator
class GroupCrudManager:
    async def create(self, course_id: int, newGroup: GroupSchema.GroupCreate, db_session: AsyncSession, create_deadline: str = None):
        newGroup_dict = newGroup.model_dump()
        group = GroupModel(course_id=course_id, create_deadline=create_deadline, **newGroup_dict)
        db_session.add(group)
        await db_session.commit()

        return group
    
    async def manual_create(self, course_id: int, newGroup: GroupSchema.GroupManualCreate, db_session: AsyncSession):
        newGroup_dict = newGroup.model_dump()
        group = GroupModel(course_id=course_id, create_deadline=None, number_of_members=len(newGroup.members), name=newGroup_dict["name"])
        db_session.add(group)
        await db_session.flush()

        for member in newGroup.members:
            stmt = (
                update(SelectedCourseModel)
                .where(SelectedCourseModel.uid == member.uid)
                .where(SelectedCourseModel.course_id == course_id)
                .values({"group_id": group.id})
            )
            await db_session.execute(stmt)

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
    
    async def get_by_course_id(self, course_id: int, db_session: AsyncSession):
        stmt = select(GroupModel).where(GroupModel.course_id == course_id)
        result = await db_session.execute(stmt)

        _list = []
        for group in result:
            await db_session.refresh(group[0], ["members"])
            for member in group[0].members:
                print(member.user_info.uid, member.user_info.name)
            _list.append({
                "id": group[0].id,
                "name": group[0].name,
                "number_of_members": group[0].number_of_members,
                "members": [{
                    "uid": member.user_info.uid,
                    "name": member.user_info.name
                } for member in group[0].members]
            })

        return _list

    
    async def join(self, uid: str, course_id: int, group_id: int, db_session: AsyncSession):
        stmt = (
            update(SelectedCourseModel)
            .where(SelectedCourseModel.uid == uid)
            .where(SelectedCourseModel.course_id == course_id)
            .values({"group_id": group_id})
        )
        await db_session.execute(stmt)
        await db_session.commit()

        return
    
    async def exit(self, uid: str, course_id: int, db_session: AsyncSession):
        stmt = (
            update(SelectedCourseModel)
            .where(SelectedCourseModel.uid == uid)
            .where(SelectedCourseModel.course_id == course_id)
            .values({"group_id": None})
        )
        await db_session.execute(stmt)
        await db_session.commit()

        return
    