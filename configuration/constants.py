from common.utils.paths import PROJECT_ROOT

ENV_PREFIX = "TMPAUTH_"
SERVICE_NAME_UPPER = "TMPAUTH"
SERVICE_NAME_LOWER = "tmpauth"
SERVICE_PATH = PROJECT_ROOT.joinpath(SERVICE_NAME_LOWER)
SETTINGS_PATH = PROJECT_ROOT.joinpath("configuration/settings.py")
TEMPLATE_PATH = PROJECT_ROOT.joinpath("templates")
MIGRATION_PATH = PROJECT_ROOT.joinpath(f"{SERVICE_NAME_LOWER}/db/service_db/migrations")
MIGRATION_MODULE = f"{SERVICE_NAME_LOWER}.db.service_db.migrations"
NO_LOG_URLS: tuple[str, ...] = (
    "/api/health",
    "/metrics",
    "/api/docs",
    "/api/openapi.json",
)
