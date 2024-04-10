from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database.mysql import crud_class_decorator
from models.selected_course import SelectedCourse as SelectedCourseModel
from schemas import selected_course as SelectedCourseSchema


@crud_class_decorator
class SelectedCourseCrudManager:
    async def create(self, uid: str, course_id: str, newRow: SelectedCourseSchema.SelectedCourseCreate, db_session: AsyncSession):
        newRow_dict = newRow.model_dump()
        selected_course = SelectedCourseModel(uid=uid, course_id=course_id, **newRow_dict)
        db_session.add(selected_course)
        await db_session.commit()

        return selected_course
    
    async def get(self, uid: str, course_id: str, db_session: AsyncSession):
        stmt = (
            select(SelectedCourseModel)
            .where(SelectedCourseModel.uid == uid)
            .where(SelectedCourseModel.course_id == course_id)
        )
        result = await db_session.execute(stmt)
        selected_course = result.first()

        return selected_course[0] if selected_course else None
    
    async def get_all(self, db_session: AsyncSession):
        stmt = select(SelectedCourseModel)
        result = await db_session.execute(stmt)
        result = result.unique()

        return [selected_course[0] for selected_course in result.all()]    
    
    async def update(self, uid: str, course_id: str, updateRow: SelectedCourseSchema.SelectedCourseUpdate, db_session: AsyncSession):
        updateRow_dict = updateRow.model_dump(exclude_none=True)
        if updateRow_dict:
            stmt = (
                update(SelectedCourseModel)
                .where(SelectedCourseModel.uid == uid)
                .where(SelectedCourseModel.course_id == course_id)
                .values(updateRow_dict)
            )
            await db_session.execute(stmt)
            await db_session.commit()

        return 
    
    async def delete(self, uid: str, course_id: str, db_session: AsyncSession):
        stmt = (
            delete(SelectedCourseModel)
            .where(SelectedCourseModel.uid == uid)
            .where(SelectedCourseModel.course_id == course_id)
        )
        await db_session.execute(stmt)
        await db_session.commit()

        return
    
    async def get_by_uid(self, uid: str, db_session: AsyncSession):
        stmt = (
            select(SelectedCourseModel)
            .where(SelectedCourseModel.uid == uid)
        )
        result = await db_session.execute(stmt)
        result = result.unique()

        return [selected_course[0] for selected_course in result.all()]
    
    async def get_by_course_id(self, course_id: str, db_session: AsyncSession):
        stmt = (
            select(SelectedCourseModel)
            .where(SelectedCourseModel.course_id == course_id)
        )
        result = await db_session.execute(stmt)
        result = result.unique()

        return [selected_course[0] for selected_course in result.all()]
    