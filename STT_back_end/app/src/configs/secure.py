from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from pydantic_settings import BaseSettings


class SecureConfig(BaseSettings):
    algorithm: str = 'HS256'
    secret_key: str = '4h3b24yu2f4uv4ut2t34c2ty34c2y4yy'


config = SecureConfig()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/users/login')
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

