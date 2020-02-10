from starlette.testclient import TestClient
from starlette.responses import JSONResponse
from starlette.applications import Starlette
from starlette.middleware import Middleware

from src.ErrorHandler import exception_handlers
from src.routes.v1 import v1

from src import settings

from src.middleware.Authentication import JWTAuthMiddleware
from starlette.middleware.authentication import AuthenticationMiddleware

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

client = TestClient(app)


def test_health():
    response = client.get(v1.path + '/health')
    assert response.status_code == 200
    assert response.json() == {}


def test_get_users_unauthorized():
    response = client.get(v1.path + '/users')

    payload = {
        'code': 403,
        'error': 'Forbidden',
    }

    assert response.status_code == 403
    assert response.json() == payload
