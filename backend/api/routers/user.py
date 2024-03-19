from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from .depends import check_user_id
from auth.jwt import verify_access_token
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
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")
    
    newUser.password = get_password_hash(newUser.password)
    user = await UserCrud.create_user(newUser)
    return user


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
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist")

    
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
async def update_user_password(
    updateUser: UserSchema.UserUpdatePassword, 
    uid: str = Depends(check_user_id),
    token:str = Depends(OAuth2PasswordBearer(tokenUrl="api/auth/login"))
) -> None:
    """
    Update the password of the particular user.
    """
    payload = await verify_access_token(token)
    if payload.get("uid") != uid:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Permission denied")
    
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
