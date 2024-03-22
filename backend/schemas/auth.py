from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer 
from pydantic import BaseModel
from typing import Annotated

oauth2_token_scheme = Annotated[str, Depends(OAuth2PasswordBearer(tokenUrl="api/auth/login"))]
login_form_schema = Annotated[OAuth2PasswordRequestForm, Depends()]


class Token(BaseModel):
    access_token: str
    token_type: str
    