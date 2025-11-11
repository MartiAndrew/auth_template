from fastapi import APIRouter
from tmpauth.db.schemas.user import UserCreate, UserRead
from tmpauth.services.authentication.auth_backend import authentication_backend
from tmpauth.services.authentication.fastapi_users import fastapi_users

from configuration.settings import settings

auth_router = APIRouter()

auth_router.include_router(
    router=fastapi_users.get_auth_router(
        authentication_backend,
        requires_verification=settings.auth.require_email_verification,
    ),
)

auth_router.include_router(
    router=fastapi_users.get_register_router(UserRead, UserCreate),
)

auth_router.include_router(router=fastapi_users.get_verify_router(UserRead))

auth_router.include_router(router=fastapi_users.get_reset_password_router())
