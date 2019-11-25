import json
import werkzeug.exceptions
from enum import Enum

class ErrorType(Enum):
    # 400 Errors
    generic = werkzeug.exceptions.BadRequest
    unauthorized = werkzeug.exceptions.Unauthorized
    forbidden = werkzeug.exceptions.Forbidden
    not_found = werkzeug.exceptions.NotFound
    too_many_requests = werkzeug.exceptions.TooManyRequests

    # 500 Errors
    internal = werkzeug.exceptions.InternalServerError
    not_implemented = werkzeug.exceptions.NotImplemented


def Error(error_type: ErrorType, message: str) -> werkzeug.exceptions.HTTPException:
    if type(error_type) is not ErrorType:
        raise Exception('Somethings wrong')
    return error_type.value(message)

# Error handler
def error_handler(error):
    response = error.get_response()
    response.data = json.dumps({
        'code': error.code,
        'name': error.name,
        'description': error.description
    })
    response.content_type = 'application/json'
    return response
