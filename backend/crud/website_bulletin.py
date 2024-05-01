from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from crud.component import ComponentCrudManager
from database.mysql import crud_class_decorator
from models.bulletin import WebsiteBulletin as WebsiteBulletinModel
from models.component import Component as ComponentModel
from schemas import bulletin as BulletinSchema

ComponentCrud = ComponentCrudManager()


@crud_class_decorator
class WebsiteBulletinCrudManager:
    async def create(self, uid: str, newBulletin: BulletinSchema.BulletinCreate, db_session: AsyncSession):
        _dict = newBulletin.model_dump()

        # Add Component
        newComponent_dict = {key: value for key, value in _dict.items() if key != "pin_to_top"}
        component = await ComponentCrud.create(uid=uid, newComponent=newComponent_dict)

        # Add WebsiteBulletin
        newBulletin_dict = {key: value for key, value in _dict.items() if key == "pin_to_top"}
        bulletin = WebsiteBulletinModel(id=component.id, **newBulletin_dict)
        db_session.add(bulletin)
        await db_session.commit()

        return bulletin

    async def get(self, bulletin_id: str, db_session: AsyncSession):
        stmt = select(WebsiteBulletinModel).where(WebsiteBulletinModel.id == bulletin_id)
        result = await db_session.execute(stmt)
        bulletin = result.first()
    
        obj = {}
        if bulletin:
            await db_session.refresh(bulletin[0], ["info"])
            obj = {
                "id": bulletin[0].id,
                "publisher": bulletin[0].info.publisher_info.name,
                "publisher_avatar": bulletin[0].info.publisher_info.avatar,
                "release_time": bulletin[0].info.release_time,
                "title": bulletin[0].info.title,
                "content": bulletin[0].info.content,
                "pin_to_top": bulletin[0].pin_to_top,
                "files": bulletin[0].info.files
            }
        
        return obj

    async def get_all(self, db_session: AsyncSession):
        stmt = select(WebsiteBulletinModel)
        result = await db_session.execute(stmt)
        
        _list = []
        for bulletin in result:
            await db_session.refresh(bulletin[0], ["info"])
            _list.append({
                "id": bulletin[0].id,
                "publisher": bulletin[0].info.publisher_info.name,
                "release_time": bulletin[0].info.release_time,
                "title": bulletin[0].info.title,
                "pin_to_top": bulletin[0].pin_to_top
            })
        
        return _list

    async def update(self, bulletin_id: str, updateBulletin: BulletinSchema.BulletinUpdate, db_session: AsyncSession):
        _dict = updateBulletin.model_dump(exclude_none=True)

        # Update Component
        updateComponent_dict = {key: value for key, value in _dict.items() if key != "pin_to_top"}
        await ComponentCrud.update(bulletin_id, updateComponent_dict)

        # Update WebsiteBulletin
        updateBulletin_dict = {key: value for key, value in _dict.items() if key == "pin_to_top"}
        if updateBulletin_dict:
            stmt = update(WebsiteBulletinModel).where(WebsiteBulletinModel.id == bulletin_id).values(**updateBulletin_dict)
            await db_session.execute(stmt)
        
        await db_session.commit()

        return
    
    async def delete(self, bulletin_id: int, db_session: AsyncSession):
        stmt = delete(ComponentModel).where(ComponentModel.id == bulletin_id)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    