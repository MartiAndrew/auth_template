from fastapi_users.authentication import AuthenticationBackend

from tmpauth.services.auth.strategy import get_database_strategy
from tmpauth.services.auth.transport import bearer_transport

authentication_backend = AuthenticationBackend(
    name="access-tokens-db",
    transport=bearer_transport,
    get_strategy=get_database_strategy,
)
