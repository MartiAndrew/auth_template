__all__ = ("templates",)

from starlette.templating import Jinja2Templates

from configuration.constants import SERVICE_PATH

templates = Jinja2Templates(
    directory=SERVICE_PATH / "templates",
)
