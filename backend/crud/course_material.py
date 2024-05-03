from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database.mysql import crud_class_decorator
from models.component import Component as ComponentModel
from models.course_material import CourseMaterial as CourseMaterialModel
from schemas import course_material as CourseMaterialSchema


@crud_class_decorator
class CourseMaterialCrudManager:
    async def create(self, uid: str, course_id: str, newCourseMaterial: CourseMaterialSchema.CourseMaterialCreate, db_session: AsyncSession):
        newCourseMaterial_dict = newCourseMaterial.model_dump()
        course_material = CourseMaterialModel(**newCourseMaterial_dict, uid=uid, course_id=course_id)
        db_session.add(course_material)
        await db_session.commit()

        return course_material
    
    async def get(self, course_material_id: str, db_session: AsyncSession):
        stmt = select(CourseMaterialModel).where(CourseMaterialModel.id == course_material_id)
        result = await db_session.execute(stmt)
        course_material = result.first()
        
        return course_material[0] if course_material else None
    
    async def get_all(self, db_session: AsyncSession):
        stmt = select(CourseMaterialModel)
        result = await db_session.execute(stmt)
        result = result.unique()
        
        return [course_material[0] for course_material in result.all()]
    
    async def update(self, course_material_id: str, updateCourseMaterial: CourseMaterialSchema.CourseMaterialUpdate, db_session: AsyncSession):
        updateCourseMaterial_dict = updateCourseMaterial.model_dump(exclude_none=True)
        if updateCourseMaterial_dict:
            stmt = update(ComponentModel).where(ComponentModel.id == course_material_id).values(**updateCourseMaterial_dict)
            await db_session.execute(stmt)
            await db_session.commit()

        return
    
    async def delete(self, course_material_id: int, db_session: AsyncSession):
        stmt = delete(ComponentModel).where(ComponentModel.id == course_material_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    