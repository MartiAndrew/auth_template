from pydantic_settings import BaseSettings, SettingsConfigDict

from common.utils.paths import PROJECT_ROOT

from configuration.constants import ENV_PREFIX, SERVICE_NAME_LOWER


class MailSettings(BaseSettings):
    """Настройки приложения отправки писем."""

    model_config = SettingsConfigDict(
        env_prefix=f"{ENV_PREFIX}MAIL_",
        env_file=PROJECT_ROOT.joinpath(".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    admin_email: str = "admin@site.com"

    host: str = "0.0.0.0"  # noqa: S104
    port: int = 1025
