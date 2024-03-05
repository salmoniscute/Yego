import hashlib
from database.mysql import crud_class_decorator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from models.user import User as UserModel
from schemas import user as UserSchema


@crud_class_decorator
class UserCrudManager:
    async def create_user(self, newUser: UserSchema.UserCreate, db_session: AsyncSession):
        user = UserModel(
            uid=newUser.uid,
            password=newUser.password,
            name=newUser.name,
            role=newUser.role,
            email=newUser.email, 
            department=newUser.department,
            country=newUser.country,
            introduction=newUser.introduction,
            avatar=newUser.avatar
        )
        db_session.add(user)
        await db_session.commit()
        db_session.refresh(user)

        return user

    async def get_user_by_id(self, uid: str, db_session: AsyncSession):
        stmt = select(
            UserModel.uid, 
            UserModel.name, 
            UserModel.role,
            UserModel.email,
            UserModel.department,
            UserModel.country,
            UserModel.introduction,
            UserModel.avatar
        ).where(UserModel.uid == uid)
        result = await db_session.execute(stmt)
        user = result.first()

        if user:
            return user
        
        return None

    async def update_user_by_id(self, uid: str, updateUser: UserSchema.UserUpdate, db_session: AsyncSession):
        stmt = update(UserModel).where(UserModel.uid == uid).values(
            name=updateUser.name, 
            role=updateUser.role,
            email=updateUser.email,
            department=updateUser.department,
            country=updateUser.country,
            introduction=updateUser.introduction,
            avatar=updateUser.avatar
        )
        await db_session.execute(stmt)
        await db_session.commit()

        return 
    
    async def update_user_password_by_id(self, uid: str, updateUser: UserSchema.UserUpdatePassword, db_session: AsyncSession):
        stmt = update(UserModel).where(UserModel.uid == uid).values(
            password=hashlib.md5(updateUser.password.encode() + b"secret").hexdigest()
        )

        await db_session.execute(stmt)
        await db_session.commit()

        return
    
    async def delete_user_by_id(self, uid: int, db_session: AsyncSession):
        stmt = delete(UserModel).where(UserModel.uid == uid)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    