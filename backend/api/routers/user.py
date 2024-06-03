import os
from fastapi import APIRouter, Depends, HTTPException, status, UploadFile
from fastapi.security import OAuth2PasswordBearer

from .depends import check_user_id
from auth.jwt import verify_token
from auth.passwd import get_password_hash
from crud.user import UserCrudManager
from models.base import Avatar
from schemas import user as UserSchema

permission_denied = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN, 
    detail="Permission denied"
)

not_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, 
    detail="User does not exist"
)

already_exists = HTTPException(
    status_code=status.HTTP_409_CONFLICT, 
    detail="User already exists"
)

UserCrud = UserCrudManager()
router = APIRouter(
    prefix="/api",
    tags=["Users"]
)


@router.post(
    "/user",
    status_code=status.HTTP_204_NO_CONTENT
)
async def create_user(newUser: UserSchema.UserCreate):
    """
    Create a user with the following information:
    - **uid**
    - **password**
    - **name**
    - **role**
    - **email**
    - **department**
    - **country**
    """
    if await UserCrud.get(newUser.uid):
        raise already_exists
    
    newUser.password = get_password_hash(newUser.password)
    user = await UserCrud.create(newUser)

    return user

    
@router.get(
    "/users",
    response_model=list[UserSchema.UserRead],
    status_code=status.HTTP_200_OK
)
async def get_all_users():
    """
    Get all users.
    """
    users = await UserCrud.get_all()
    if users:
        return users
    
    raise not_found


@router.get(
    "/user/{uid}",
    response_model=UserSchema.UserRead,
    status_code=status.HTTP_200_OK
)
async def get_user(uid: str):
    """
    Get the particular user.
    """
    user = await UserCrud.get(uid)
    if user:
        return user
    
    raise not_found


@router.get(
    "/user/search/{keyword}",
    response_model=list[UserSchema.UserRead],
    status_code=status.HTTP_200_OK
)
async def search_user(keyword: str=None):
    users = await UserCrud.search(keyword)
    if users:
        return users
    raise not_found


@router.put(
    "/user/{uid}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_user(
    updateUser: UserSchema.UserUpdate, 
    uid: str = Depends(check_user_id),
    # token: str = Depends(OAuth2PasswordBearer(tokenUrl="api/auth/login"))
):
    """
    Update the user with at least one of the following information:
    - **name**
    - **role**
    - **email**
    - **department**
    - **country**
    - **introduction**
    """
    # payload = await verify_access_token(token)
    # if payload.get("uid") != uid:
    #     raise permission_denied
    
    await UserCrud.update(uid, updateUser)
    return 


@router.put(
    "/user/{uid}/default_avatar",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_user_role(
    avatar: Avatar,
    uid: str = Depends(check_user_id)
):
    await UserCrud.update_avatar(uid, f"/assets/{avatar}.png")
    return 


@router.put(
    "/user/{uid}/avatar",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_user_avatar(
    avatar: UploadFile,
    uid: str = Depends(check_user_id),
    # token: str = Depends(OAuth2PasswordBearer(tokenUrl="api/auth/login"))
):
    """
    Update the user avatar.
    """
    # payload = await verify_access_token(token)
    # if payload.get("uid") != uid:
    #     raise permission_denied
    
    avatar_path = None
    if avatar:
        public_dir = "../frontend/public"
        avatar_dir = f"assets/upload/user/{uid}"
        if not os.path.isdir(f"{public_dir}/{avatar_dir}"):
            os.makedirs(f"{public_dir}/{avatar_dir}")
        
        with open(f"{public_dir}/{avatar_dir}/{avatar.filename}", "wb") as file:
            content = await avatar.read()  
            file.write(content)
        
        avatar_path = f"{avatar_dir}/{avatar.filename}"
    
    await UserCrud.update_avatar(uid, f"/{avatar_path}")
    return 


@router.put(
    "/user/{uid}/password",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_user_password(
    updateUser: UserSchema.UserUpdatePassword, 
    uid: str = Depends(check_user_id),
    # token:str = Depends(OAuth2PasswordBearer(tokenUrl="api/auth/login"))
):
    """
    Update the password of the particular user.
    """
    # payload = await verify_access_token(token)
    # if payload.get("uid") != uid:
    #     raise permission_denied
    
    await UserCrud.update_password(uid, updateUser)

    return 
    

@router.delete(
    "/user/{uid}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_user(uid: str = Depends(check_user_id)):
    """
    Delete the user.
    """
    await UserCrud.delete(uid)
    return 
