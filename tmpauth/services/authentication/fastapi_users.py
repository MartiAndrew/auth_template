from fastapi_users import FastAPIUsers

from configuration.types import UserIdType
from tmpauth.db.models import User
from tmpauth.services.authentication.auth_backend import authentication_backend
from tmpauth.services.authentication.dependencies import get_user_manager

fastapi_users = FastAPIUsers[User, UserIdType](
    get_user_manager,
    [authentication_backend],
)
