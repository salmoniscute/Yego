from fastapi import HTTPException

from crud.user import UserCrudManager

UserCrud = UserCrudManager()


async def check_user_id(uid: str):
    user = await UserCrud.get_user_by_id(uid)
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist")
    
    return user.uid
