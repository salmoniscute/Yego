from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database.mysql import crud_class_decorator
from models.course import Course as CourseModel
from schemas import course as CourseSchema


@crud_class_decorator
class CourseCrudManager:
    async def create(self, uid: str, newCourse: CourseSchema.CourseCreate, db_session: AsyncSession):
        newCourse_dict = newCourse.model_dump()
        course = CourseModel(**newCourse_dict, uid=uid)
        db_session.add(course)
        await db_session.commit()

        return course
     
    async def get(self, course_id: str, db_session: AsyncSession):
        stmt = select(CourseModel).where(CourseModel.id == course_id)
        result = await db_session.execute(stmt)
        course = result.first()
        
        return course[0] if course else None

    async def get_all(self, db_session: AsyncSession):
        stmt = select(CourseModel)
        result = await db_session.execute(stmt)
        result = result.unique()
        
        return [course[0] for course in result.all()]
    
    async def update(self, course_id: str, updateCourse: CourseSchema.CourseUpdate, db_session: AsyncSession):
        updateCourse_dict = updateCourse.model_dump(exclude_none=True)
        if updateCourse_dict:
            stmt = update(CourseModel).where(CourseModel.id == course_id).values(**updateCourse_dict)
            await db_session.execute(stmt)
            await db_session.commit()

        return 
    
    async def delete(self, course_id: int, db_session: AsyncSession):
        stmt = delete(CourseModel).where(CourseModel.id == course_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    