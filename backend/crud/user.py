from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from auth.passwd import get_password_hash
from database.mysql import crud_class_decorator
from models.user import User as UserModel
from schemas import user as UserSchema


@crud_class_decorator
class UserCrudManager:
    async def create(self, newUser: UserSchema.UserCreate, db_session: AsyncSession):
        newUser_dict = newUser.model_dump()
        user = UserModel(avatar=None, introduction=None, **newUser_dict)
        db_session.add(user)
        await db_session.commit()

        return user

    async def get(self, uid: str, db_session: AsyncSession):
        stmt = select(UserModel).where(UserModel.uid == uid)
        result = await db_session.execute(stmt)
        user = result.first()
        
        return user[0] if user else None
    
    async def get_all(self, db_session: AsyncSession):
        stmt = select(UserModel)
        result = await db_session.execute(stmt)
        result = result.unique()

        return [user[0] for user in result.all()]

    async def update(self, uid: str, updateUser: UserSchema.UserUpdate, db_session: AsyncSession):
        updateUser_dict = updateUser.model_dump(exclude_none=True)
        if updateUser_dict:
            stmt = update(UserModel).where(UserModel.uid == uid).values(updateUser_dict)
            await db_session.execute(stmt)
            await db_session.commit()

        return 
    
    async def update_password(self, uid: str, updateUser: UserSchema.UserUpdatePassword, db_session: AsyncSession):
        updateUser_dict = {"password": get_password_hash(updateUser.password)}
        stmt = update(UserModel).where(UserModel.uid == uid).values(updateUser_dict)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    
    async def update_avatar(self, uid: str, avatar_path: str, db_session: AsyncSession):
        updateUser_dict = {"avatar": avatar_path}
        stmt = update(UserModel).where(UserModel.uid == uid).values(updateUser_dict)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    
    async def delete(self, uid: int, db_session: AsyncSession):
        stmt = delete(UserModel).where(UserModel.uid == uid)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    
    async def login(self, uid: str, db_session: AsyncSession):
        stmt = select(
            UserModel.uid, 
            UserModel.password,
            UserModel.role,
            UserModel.name,
            UserModel.country,
            UserModel.department,
            UserModel.email,
            UserModel.introduction,
            UserModel.avatar
        ).where(UserModel.uid == uid)
        result = await db_session.execute(stmt)
        user = result.first()

        return user if user else None
    
    async def search(self, keyword: str, db_session: AsyncSession):
        output = []
        stmt = select(UserModel).where(UserModel.name.like(f"%{keyword}%"))
        result = await db_session.execute(stmt)
        result = result.unique()
        for user in result.all():
            output.append({
                "uid": user[0].uid,
                "name": user[0].name,
                "role": user[0].role,
                "country": user[0].country,
                "department": user[0].department,
                "email": user[0].email,
                "introduction": user[0].introduction,
                "avatar": user[0].avatar
            })
        
        stmt = select(UserModel).where(UserModel.uid.like(f"%{keyword}%"))
        result = await db_session.execute(stmt)
        result = result.unique()
        for user in result.all():
            output.append({
                "uid": user[0].uid,
                "name": user[0].name,
                "role": user[0].role,
                "country": user[0].country,
                "department": user[0].department,
                "email": user[0].email,
                "introduction": user[0].introduction,
                "avatar": user[0].avatar
            })
            
        stmt = select(UserModel).where(UserModel.role.like(f"%{keyword}%"))
        result = await db_session.execute(stmt)
        result = result.unique()
        for user in result.all():
            output.append({
                "uid": user[0].uid,
                "name": user[0].name,
                "role": user[0].role,
                "country": user[0].country,
                "department": user[0].department,
                "email": user[0].email,
                "introduction": user[0].introduction,
                "avatar": user[0].avatar
            })
            
        stmt = select(UserModel).where(UserModel.country.like(f"%{keyword}%"))
        result = await db_session.execute(stmt)
        result = result.unique()
        for user in result.all():
            output.append({
                "uid": user[0].uid,
                "name": user[0].name,
                "role": user[0].role,
                "country": user[0].country,
                "department": user[0].department,
                "email": user[0].email,
                "introduction": user[0].introduction,
                "avatar": user[0].avatar
            })
            
        stmt = select(UserModel).where(UserModel.department.like(f"%{keyword}%"))
        result = await db_session.execute(stmt)
        result = result.unique()
        for user in result.all():
            output.append({
                "uid": user[0].uid,
                "name": user[0].name,
                "role": user[0].role,
                "country": user[0].country,
                "department": user[0].department,
                "email": user[0].email,
                "introduction": user[0].introduction,
                "avatar": user[0].avatar
            })
        
               
        
        return output
    