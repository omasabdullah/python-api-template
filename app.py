import logging
import uvicorn

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.middleware import Middleware

from src.middleware.Logging import LoggingMiddleware
from src.ErrorHandler import exception_handlers
from src.routes.v1 import v1
from src.routes.graphql import graphql_route

from src.middleware.Authentication import AuthMiddleware
from starlette.middleware.authentication import AuthenticationMiddleware



routes = [
    v1,
    graphql_route
]

middleware = [
    Middleware(LoggingMiddleware),
    Middleware(AuthenticationMiddleware, backend=AuthMiddleware())
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
