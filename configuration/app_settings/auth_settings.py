from pydantic_settings import BaseSettings, SettingsConfigDict

from common.utils.paths import PROJECT_ROOT

from configuration import types
from configuration.constants import ENV_PREFIX, SERVICE_NAME_LOWER


class AuthSettings(BaseSettings):
    """Настройки аутентификации приложения."""

    model_config = SettingsConfigDict(
        env_prefix=f"{ENV_PREFIX}AUTH_",
        env_file=PROJECT_ROOT.joinpath(".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # время жизни access токена
    lifetime_seconds: int = 3600

    reset_password_token_secret: str = ""

    verification_token_secret: str = ""

    #token_url for transport
    bearer_token_url: str = f"api/{SERVICE_NAME_LOWER}/auth/login"



