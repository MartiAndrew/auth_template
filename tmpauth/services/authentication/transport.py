from fastapi_users.authentication import BearerTransport, CookieTransport

from configuration.settings import settings

bearer_transport = BearerTransport(
    tokenUrl=settings.auth.bearer_token_url,
)

cookie_transport = CookieTransport(
    cookie_max_age=settings.auth.cookie_max_age,
    cookie_secure=settings.auth.cookie_secure,
)
