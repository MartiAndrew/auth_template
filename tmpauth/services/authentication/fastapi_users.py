from fastapi_users import FastAPIUsers
from tmpauth.db.models import User
from tmpauth.services.authentication.auth_backend import authentication_backend
from tmpauth.services.authentication.dependencies import get_user_manager

from configuration.types import UserIdType

fastapi_users = FastAPIUsers[User, UserIdType](
    get_user_manager,
    [authentication_backend],
)

current_active_user = fastapi_users.current_user(active=True)
current_super_user = fastapi_users.current_user(active=True, superuser=True)
