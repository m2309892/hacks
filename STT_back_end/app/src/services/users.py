from datetime import datetime, timedelta
import jwt
from fastapi import HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from src.configs.secure import pwd_context, config, oauth2_scheme
from src.databases.models.users import User
from src.dependencies.base import get_async_session
from src.repositories.users import UserRepository
from src.schemas.users import TokenData, CreateUserDTO


users_repository = UserRepository()


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


async def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=7)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(
        to_encode,
        config.secret_key,
        algorithm=config.algorithm
    )
    return encoded_jwt


def verify_access_token(token: str):
    credentials_exception = HTTPException(status.HTTP_401_UNAUTHORIZED, 'Не удалось авторизироваться')
    try:
        payload = jwt.decode(token, config.secret_key, algorithms=[config.algorithm])
        user_id = payload.get('user_id')

        if user_id is None:
            raise credentials_exception
        token_data = TokenData(user_id=user_id)
    except Exception:
        raise credentials_exception

    return token_data


async def register_user(data: CreateUserDTO):
    data.password = hash_password(data.password)

    return await users_repository.create(data)


async def login_user(email: str, password: str):
    user = await auth_user(email, password)
    access_token = await create_access_token({'user_id': user.id})

    user_data = {
        'access_token': access_token,
        'token_type': 'bearer'
    }
    return user_data


async def auth_user(email: str, password: str):
    user = await users_repository.get_one_by(User.email == email, False)

    if not (user and verify_password(password, user.password)):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, 'Неверный логин или пароль.')

    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    token = verify_access_token(token)

    user = await users_repository.get(token.user_id)

    if user is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, 'Не удалось авторизироваться')

    return user





