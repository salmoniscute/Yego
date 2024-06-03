from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database.mysql import crud_class_decorator
from models.selected_course import SelectedCourse as SelectedCourseModel
from schemas import selected_course as SelectedCourseSchema


@crud_class_decorator
class SelectedCourseCrudManager:
    async def create(self, uid: str, course_id: int, db_session: AsyncSession, group_id: int = None):
        selected_course = SelectedCourseModel(uid=uid, course_id=course_id, group_id=group_id)
        db_session.add(selected_course)
        await db_session.commit()

        return selected_course
    
    async def get(self, uid: str, course_id: int, db_session: AsyncSession):
        stmt = (
            select(SelectedCourseModel)
            .where(SelectedCourseModel.uid == uid)
            .where(SelectedCourseModel.course_id == course_id)
        )
        result = await db_session.execute(stmt)
        selected_course = result.first()
        if selected_course:
            await db_session.refresh(selected_course[0], ["group_info"])

        return selected_course[0] if selected_course else None
    
    async def get_all(self, db_session: AsyncSession):
        stmt = select(SelectedCourseModel)
        result = await db_session.execute(stmt)
        result = result.unique()

        return [selected_course[0] for selected_course in result.all()]    
    
    async def update(self, uid: str, course_id: int, group_id: int, db_session: AsyncSession):
        stmt = (
            update(SelectedCourseModel)
            .where(SelectedCourseModel.uid == uid)
            .where(SelectedCourseModel.course_id == course_id)
            .values({"group_id": group_id})
        )
        await db_session.execute(stmt)
        await db_session.commit()

        return 
    
    async def delete(self, uid: str, course_id: int, db_session: AsyncSession):
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

        _list = []
        for selected_course in result:
            _list.append({
                "course_id": selected_course[0].course_id,
                "instructor_name": selected_course[0].course_info.instructor_info.name,
                "course_code": selected_course[0].course_info.course_code,
                "academic_year": selected_course[0].course_info.academic_year,
                "semester": selected_course[0].course_info.semester,
                "course_name": selected_course[0].course_info.name,
                "outline": selected_course[0].course_info.outline
            })

        return _list
    
    async def get_by_course_id(self, course_id: int, db_session: AsyncSession):
        stmt = (
            select(SelectedCourseModel)
            .where(SelectedCourseModel.course_id == course_id)
        )
        result = await db_session.execute(stmt)
        
        _list = []
        for selected_course in result:
            await db_session.refresh(selected_course[0], ["group_info"])
            _list.append({
                "uid": selected_course[0].user_info.uid,
                "name": selected_course[0].user_info.name,
                "role": selected_course[0].user_info.role,
                "department": selected_course[0].user_info.department,
                "country": selected_course[0].user_info.country,
                "email": selected_course[0].user_info.email,
                "avatar": selected_course[0].user_info.avatar,
                "introduction": selected_course[0].user_info.introduction,
                "group_name": selected_course[0].group_info.name if selected_course[0].group_info else None
            })

        return _list
