import jwt
import sqlalchemy
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, status

from models.user import User as UserModel
from schemas import auth as AuthSchema

secret = "secret"
algorithm = "HS256"

token_expired = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Token expired",
    headers={"WWW-Authenticate": "Bearer"}
)

invalid_token = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid token",
    headers={"WWW-Authenticate": "Bearer"}
)


async def create_jwt(data: sqlalchemy.engine.row.Row):
    return jwt.encode(dict(data._mapping), secret, algorithm)


async def create_access_token(data: UserModel):
    expire = datetime.now(tz=timezone.utc) + timedelta(minutes=10)

    to_encode = data.__dict__
    to_encode.pop("_sa_instance_state")
    to_encode.pop("password")
    to_encode.update({"exp": expire})

    access_token = jwt.encode(to_encode, secret, algorithm)

    return AuthSchema.Token(access_token=access_token, token_type="bearer")


async def verify_access_token(token: str):
    try:
        print(token)
        return jwt.decode(token, secret, algorithm)
    
    except jwt.ExpiredSignatureError:
        raise token_expired
    
    except jwt.exceptions.InvalidTokenError:
        raise invalid_token
    