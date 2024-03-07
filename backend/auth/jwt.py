import jwt
import sqlalchemy


secret = "secret"
algorithm = "HS256"
def create_jwt(data: sqlalchemy.engine.row.Row):
    return jwt.encode(dict(data._mapping), secret, algorithm)