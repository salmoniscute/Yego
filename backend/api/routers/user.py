from fastapi import APIRouter, Depends, HTTPException, status

from .depends import check_user_id
from auth.passwd import get_password_hash
from crud.user import UserCrudManager
from schemas import user as UserSchema

UserCrud = UserCrudManager()
router = APIRouter(
    prefix="/api",
    tags=["Users"]
)


@router.post(
    "/user",
    response_model=UserSchema.UserCreateResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_user(newUser: UserSchema.UserCreate) -> dict:
    """
    Create a user with the following information:
    - **uid**
    - **password**
    - **name**
    - **role**
    - **email**
    - **department**
    - **country**
    - **introduction** (optional)
    - **avatar** (optional)
    """
    user = await UserCrud.get_user_by_id(newUser.uid)
    if user:
        raise HTTPException(status_code=409, detail="User already exists")
    
    newUser.password = get_password_hash(newUser.password)
    user = await UserCrud.create_user(newUser)
    return user


@router.get(
    "/users",
)
async def get_users() -> list:
    return []


@router.get(
    "/user/{uid}",
    response_model=UserSchema.UserRead
)
async def get_user(uid: str) -> dict:
    """
    Get the information of the particular user.
    """
    user = await UserCrud.get_user_by_id(uid)
    if user:
        return user
    
    raise HTTPException(status_code=404, detail="User does not exists")

    
@router.put(
    "/user/{uid}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_user(updateUser: UserSchema.UserUpdate, uid: str = Depends(check_user_id)) -> None:
    """
    Update the information of the particular user with at least one of the following information:
    - **name**
    - **role**
    - **email**
    - **department**
    - **country**
    - **introduction**
    - **avatar**
    """
    await UserCrud.update_user_by_id(uid, updateUser)
    return 
    

@router.put(
    "/user/{uid}/password",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_user_password(updateUser: UserSchema.UserUpdatePassword, uid: str = Depends(check_user_id)) -> None:
    """
    Update the password of the particular user.
    """
    await UserCrud.update_user_password_by_id(uid, updateUser)
    return 
    

@router.delete(
    "/user/{uid}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_user(uid: str = Depends(check_user_id)) -> None:
    """
    Delete the particular user.
    """
    await UserCrud.delete_user_by_id(uid)
    return 
