import pytest

from starlette.testclient import TestClient
from starlette.responses import JSONResponse
from starlette.applications import Starlette
from starlette.middleware import Middleware

from src.ErrorHandler import exception_handlers
from src.routes.v1 import v1

from src import settings

from src.middleware.Authentication import JWTAuthMiddleware
from starlette.middleware.authentication import AuthenticationMiddleware


@pytest.fixture
def client():
    routes = [
        v1
    ]

    middleware = [
        Middleware(AuthenticationMiddleware, backend=JWTAuthMiddleware())
    ]

    app = Starlette(
        debug=settings.DEBUG,
        routes=routes,
        exception_handlers=exception_handlers,
        middleware=middleware
    )

    yield TestClient(app)
