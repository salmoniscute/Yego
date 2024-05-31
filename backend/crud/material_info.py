from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from crud.component import ComponentCrudManager
from database.mysql import crud_class_decorator
from models.course_material import MaterialInfo as MaterialInfoModel
from schemas import course_material as CourseMaterialSchema

ComponentCrud = ComponentCrudManager()


@crud_class_decorator
class MaterialInfoCrudManager:
    async def create(self, uid: str, course_material_id: int, newMaterialInfo: CourseMaterialSchema.MaterialInfoCreate, db_session: AsyncSession):
        obj = {
            "title": newMaterialInfo.title,
            "content": newMaterialInfo.content,
        }
        component = await ComponentCrud.create(uid, obj)
        
        material_info = MaterialInfoModel(
            id=component.id, 
            material_id=course_material_id, 
            start_time=newMaterialInfo.start_time, 
            end_time=newMaterialInfo.end_time, 
            display=newMaterialInfo.display
        )
        db_session.add(material_info)
        await db_session.commit()

        return material_info
    
    async def get(self, material_info_id: int, db_session: AsyncSession):
        stmt = select(MaterialInfoModel).filter(MaterialInfoModel.id == material_info_id)
        result = await db_session.execute(stmt)
        material_info = result.first()
        
        return material_info
    
    async def update(self, material_info_id: int, newMaterialInfo: CourseMaterialSchema.MaterialInfoUpdate, db_session: AsyncSession):
        component = {
            "title": newMaterialInfo.title,
            "content": newMaterialInfo.content
        }
        material_info = {
            "display": newMaterialInfo.display
        }

        # Update component
        if component:
            await ComponentCrud.update(material_info_id, component)

        # Update material_info
        if material_info:
            await ComponentCrud.update(material_info_id, component)
            stmt = update(MaterialInfoModel).where(MaterialInfoModel.id == material_info_id).values(material_info)
            await db_session.execute(stmt)
            await db_session.commit()

        return
    
    async def delete(self, material_info_id: int, db_session: AsyncSession):
        await ComponentCrud.delete(material_info_id)
        stmt = delete(MaterialInfoModel).where(MaterialInfoModel.id == material_info_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return