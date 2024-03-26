from database.mysql import crud_class_decorator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from models.selected_course import SelectedCourse as SelectedCourseModel
from schemas import selected_course as SelectedCourseSchema


@crud_class_decorator
class SelectedCourseCrudManager:
    async def create_selected_course(self, newRow: SelectedCourseSchema.SelectedCourseCreate, db_session: AsyncSession):
        row = SelectedCourseModel(
            uid=newRow.uid,
            course_id=newRow.course_id,
            group=newRow.group
        )
        db_session.add(row)
        await db_session.commit()
        db_session.refresh(row)

        return row

    async def get_particular_selected_course(self, uid: str, course_id: str, db_session: AsyncSession):
        stmt = (
            select(SelectedCourseModel.uid, SelectedCourseModel.course_id, SelectedCourseModel.group)
            .where(SelectedCourseModel.uid == uid)
            .where(SelectedCourseModel.course_id == course_id)
        )
        result = await db_session.execute(stmt)

        row = result.first()
        if row:
            return row
        
        return None
    
    async def get_selected_course_by_uid(self, uid: str, db_session: AsyncSession):
        stmt = (
            select(SelectedCourseModel.uid, SelectedCourseModel.course_id, SelectedCourseModel.group)
            .where(SelectedCourseModel.uid == uid)
        )
        result = await db_session.execute(stmt)

        if result:
            return result
        
        return None
    
    async def get_selected_course_by_course_id(self, course_id: str, db_session: AsyncSession):
        stmt = (
            select(SelectedCourseModel.uid, SelectedCourseModel.course_id, SelectedCourseModel.group)
            .where(SelectedCourseModel.course_id == course_id)
        )
        result = await db_session.execute(stmt)

        if result:
            return result
        
        return None

    async def update_selected_course_by_id(self, uid: str, course_id: str, updateRow: SelectedCourseSchema.SelectedCourseUpdate, db_session: AsyncSession):
        stmt = (
            update(SelectedCourseModel)
            .where(SelectedCourseModel.uid == uid)
            .where(SelectedCourseModel.course_id == course_id)
            .values(group=updateRow.group)
        )
        await db_session.execute(stmt)
        await db_session.commit()

        return 
    
    
    async def delete_selected_course_by_id(self, uid: str, course_id: str, db_session: AsyncSession):
        stmt = (
            delete(SelectedCourseModel)
            .where(SelectedCourseModel.uid == uid)
            .where(SelectedCourseModel.course_id == course_id)
        )
        await db_session.execute(stmt)
        await db_session.commit()

        return
    