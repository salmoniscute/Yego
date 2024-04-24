import os
from fastapi import APIRouter, Depends, HTTPException, status, UploadFile
from fastapi.security import OAuth2PasswordBearer

from .depends import check_user_id
from auth.jwt import verify_access_token
from auth.passwd import get_password_hash
from crud.user import UserCrudManager
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
    response_model=UserSchema.UserRead,
    status_code=status.HTTP_201_CREATED
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
        out_file_path = f"upload/user/{uid}"
        if not os.path.isdir(out_file_path):
            os.makedirs(out_file_path)
        
        with open(f"{out_file_path}/{avatar.filename}", "wb") as file:
            content = await avatar.read()  
            file.write(content)
        
        avatar_path = f"backend/{out_file_path}/{avatar.filename}"
    
    await UserCrud.update_avatar(uid, avatar_path)
    return 


@router.put(
    "/user/{uid}/password",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_user_password(
    updateUser: UserSchema.UserUpdatePassword, 
    uid: str = Depends(check_user_id),
    token:str = Depends(OAuth2PasswordBearer(tokenUrl="api/auth/login"))
):
    """
    Update the password of the particular user.
    """
    payload = await verify_access_token(token)
    if payload.get("uid") != uid:
        raise permission_denied
    
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
