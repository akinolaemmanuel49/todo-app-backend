from typing import Any, Union

from fastapi import status
from pydantic import BaseModel


class ErrorResponse(BaseModel):
    code: int
    message: Union[Any, None]


error_responses = {status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": ErrorResponse}, status.HTTP_401_UNAUTHORIZED: {
    "model": ErrorResponse}, status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": ErrorResponse}, status.HTTP_403_FORBIDDEN: {"model": ErrorResponse}, status.HTTP_404_NOT_FOUND: {"model": ErrorResponse}, status.HTTP_400_BAD_REQUEST: {"model": ErrorResponse}, status.HTTP_409_CONFLICT: {"model": ErrorResponse}}
