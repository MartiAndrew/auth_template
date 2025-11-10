from fastapi import APIRouter
from tmpauth.db.schemas.user import UserRead, UserUpdate
from tmpauth.services.authentication.fastapi_users import fastapi_users

users_router = APIRouter()

users_router.include_router(
    router=fastapi_users.get_users_router(
        UserRead,
        UserUpdate,
    ),
)
