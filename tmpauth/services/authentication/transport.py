from fastapi_users.authentication import BearerTransport

from configuration.settings import settings

bearer_transport = BearerTransport(
    tokenUrl=settings.auth.bearer_token_url,
)