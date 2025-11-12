from fastapi import APIRouter, Request
from tmpauth.jinja_templates import templates

router = APIRouter(
    prefix="/verify-email",
)


@router.get(
    "/",
    include_in_schema=False,
    name="verify_email",
)
def verify_email(
    request: Request,
):
    """
    Page Verify email.

    :param request: Обьект запроса.
    :return: Страница верификации.
    """
    return templates.TemplateResponse(
        "verification.html",
        {
            "request": request,
        },
    )
