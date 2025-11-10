from fastapi import APIRouter
from tmpauth.db.schemas.user import UserCreate, UserRead
from tmpauth.services.authentication.auth_backend import authentication_backend
from tmpauth.services.authentication.fastapi_users import fastapi_users

auth_router = APIRouter()


auth_router.include_router(router=fastapi_users.get_auth_router(authentication_backend))

auth_router.include_router(
    router=fastapi_users.get_register_router(UserRead, UserCreate)
)
