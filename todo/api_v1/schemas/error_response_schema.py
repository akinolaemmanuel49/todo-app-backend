from typing import Any, Union

from fastapi import status
from pydantic import BaseModel


class ErrorResponse(BaseModel):
    code: int
    message: Union[Any, None]


class ErrorResponse400(ErrorResponse):
    code: int = status.HTTP_400_BAD_REQUEST
    message: Union[Any, None] = "Bad Request"


class ErrorResponse401(ErrorResponse):
    code: int = status.HTTP_401_UNAUTHORIZED
    message: Union[Any, None] = "Unauthorized"


class ErrorResponse403(ErrorResponse):
    code: int = status.HTTP_403_FORBIDDEN
    message: Union[Any, None] = "Forbidden"


class ErrorResponse404(ErrorResponse):
    code: int = status.HTTP_404_NOT_FOUND
    message: Union[Any, None] = "Not Found"


class ErrorResponse409(ErrorResponse):
    code: int = status.HTTP_409_CONFLICT
    message: Union[Any, None] = "Conflict"


class ErrorResponse422(ErrorResponse):
    code: int = status.HTTP_422_UNPROCESSABLE_ENTITY
    message: Union[Any, None] = "Unprocessable Entity"


class ErrorResponse500(ErrorResponse):
    code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    message: Union[Any, None] = "Internal Server Error"


error_responses = {status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": ErrorResponse500}, status.HTTP_401_UNAUTHORIZED: {
    "model": ErrorResponse401}, status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": ErrorResponse422}, status.HTTP_403_FORBIDDEN: {"model": ErrorResponse403}, status.HTTP_404_NOT_FOUND: {"model": ErrorResponse404}, status.HTTP_400_BAD_REQUEST: {"model": ErrorResponse400}, status.HTTP_409_CONFLICT: {"model": ErrorResponse409}}
