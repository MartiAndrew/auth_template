__all__ = ("templates",)

from starlette.templating import Jinja2Templates

from configuration.constants import TEMPLATE_PATH

templates = Jinja2Templates(
    directory=TEMPLATE_PATH,
)