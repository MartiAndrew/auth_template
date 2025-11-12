from starlette import status
from tmpauth.web.error_responses import PARAMS_VALIDATION_ERR_CODE  # noqa: WPS235

from common.errors.exceptions import ServiceError
from common.errors.schema import ErrorResponse, ErrResponseBody


class ParameterValidationError(ServiceError):
    """Несоответствие параметров условиям валидации."""

    def __init__(self, parameter_name: list[str] | str):
        self.response_data = ErrorResponse(
            body=ErrResponseBody(
                message="Значение не соответствует требованиям {parameter_name}.",
                error_code=PARAMS_VALIDATION_ERR_CODE,
                verbose_message="Значение не соответствует требованиям "
                "{parameter_name}.",
                extra={"parameter_name": [parameter_name]},
            ),
            status_code=status.HTTP_400_BAD_REQUEST,
        )
