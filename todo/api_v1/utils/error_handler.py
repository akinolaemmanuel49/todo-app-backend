from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


def get_error_message(exc):
    result = []
    for error in exc.errors():
        result.append(error)
    return result


def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"message": "Validation failed", "errors": get_error_message(exc)},)
