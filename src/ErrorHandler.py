import json
from starlette.responses import JSONResponse
from starlette.exceptions import HTTPException
from starlette.authentication import AuthenticationError

from enum import Enum

class ErrorType(Enum):
    generic = 400
    unauthorized = 401
    forbidden = 403
    not_found = 404
    too_many_requests = 429

    internal = 500
    not_implemented = 501


def Error(error_type: ErrorType, detail: str) -> HTTPException:
    if type(error_type) is not ErrorType:
        raise Exception('Somethings wrong')

    return HTTPException(status_code=error_type.value, detail=detail)

# Error handler
def http_exception(request, error):
    return JSONResponse({
        'code': error.status_code,
        'error': error.detail
    }, status_code=error.status_code)

exception_handlers = {
    HTTPException: http_exception,
    AuthenticationError: http_exception,
}
