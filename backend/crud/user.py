from auth.passwd import get_password_hash
from database.mysql import crud_class_decorator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from models.user import User as UserModel
from schemas import user as UserSchema


@crud_class_decorator
class UserCrudManager:
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
    
    async def create(self, newUser: UserSchema.UserCreate, db_session: AsyncSession):
        newUser_dict = newUser.model_dump()
        user = UserModel(**newUser_dict)
        db_session.add(user)
        await db_session.commit()
        db_session.refresh(user)

        return user

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
    
    async def delete(self, uid: int, db_session: AsyncSession):
        stmt = delete(UserModel).where(UserModel.uid == uid)
        await db_session.execute(stmt)
        await db_session.commit()

        return
    