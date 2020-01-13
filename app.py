import logging
import uvicorn

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.middleware import Middleware

from src.Logging import LoggingMiddleware
from src.ErrorHandler import exception_handlers
from src.routes.v1 import v1


routes = [
    v1
]

middleware = [
    Middleware(LoggingMiddleware)
]

app = Starlette(
    debug=True,
    routes=routes,
    exception_handlers=exception_handlers,
    middleware=middleware
)


# Start server
if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=8000, log_level='info', reload=True)
