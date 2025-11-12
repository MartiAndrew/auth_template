from fastapi_users.authentication import AuthenticationBackend
from tmpauth.services.authentication.strategy import get_database_strategy
from tmpauth.services.authentication.transport import cookie_transport

authentication_backend = AuthenticationBackend(
    name="access-tokens-db",
    transport=cookie_transport,
    get_strategy=get_database_strategy,
)
