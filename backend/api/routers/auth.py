from fastapi import APIRouter, HTTPException, status

from auth.jwt import create_token_pair, verify_token
from auth.passwd import verify_password
from crud.user import UserCrudManager
from schemas import auth as AuthSchema

exception_invalid_login = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorrect username or password",
    headers={"WWW-Authenticate": "Bearer"}
)

invalid_token = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid token",
    headers={"WWW-Authenticate": "Bearer"}
)

UserCrud = UserCrudManager()
router = APIRouter(
    prefix="/api/auth",
    tags=["Users"]
)


@router.post(
    "/login",
    response_model=AuthSchema.Token
)
async def login(form_data: AuthSchema.login_form_schema):
    """
    Login with the following information:
    - **username**
    - **password**

    """
    user_in_db = await UserCrud.login(form_data.username)
    
    if user_in_db is None:
        raise exception_invalid_login
    
    if not verify_password(form_data.password, user_in_db.password):
        raise exception_invalid_login
    
    return await create_token_pair(user_in_db)


@router.post(
    "/refresh",
    response_model=AuthSchema.Token
)
async def refresh(refersh_data: AuthSchema.RefreshRequest):
    """
    Refresh token with the following information:
    - **token** 
    """
    payload: dict = await verify_token(refersh_data.refresh_token)
    if payload is None:
        raise invalid_token
    
    uid: str = payload.get("uid")
    if uid is None:
        raise invalid_token
    
    user_in_db = await UserCrud.login(uid)

    return await create_token_pair(user_in_db)
