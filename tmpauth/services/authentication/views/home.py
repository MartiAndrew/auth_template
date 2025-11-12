from typing import Annotated

from fastapi import APIRouter, Depends
from starlette.requests import Request
from tmpauth.db.models import User
from tmpauth.jinja_templates import templates
from tmpauth.services.authentication.fastapi_users import current_active_user

router = APIRouter(prefix="/home", tags=["home"])


@router.get(
    "/",
    include_in_schema=False,
    name="home",
)
def home(
    request: Request,
    user: Annotated[User, Depends(current_active_user)],
):
    """
    Home page.

    :param request: объект запроса
    :param user: текущий пользователь
    :return: шаблон страницы home.html
    """
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "user": user,
        },
    )
