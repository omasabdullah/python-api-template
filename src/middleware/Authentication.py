import base64
import binascii
import jwt

from enum import Enum

from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint

from src.models.Permissions import AuthenticationScopes
from src.ErrorHandler import Error, ErrorType
from src.controllers.AuthenticationController import authenticate_user
from src.controllers.UserController import get_user
from src import settings, strings

from src.models.User import User

from starlette.authentication import AuthenticationBackend, SimpleUser, AuthCredentials

class BasicAuthMiddleware(AuthenticationBackend):
    async def authenticate(self, request):
        if 'Authorization' not in request.headers:
            return

        auth = request.headers['Authorization']
        scheme, credentials = auth.split()
        username, password = None, None

        if scheme.lower() != 'basic':
            return

        try:
            decoded = base64.b64decode(credentials).decode('ascii')
        except (ValueError, UnicodeDecodeError, binascii.Error) as e:
            return

        username, _, password = decoded.partition(':')

        if await authenticate_user(
            email=username,
            password=password
        ):
            return AuthCredentials([AuthenticationScopes.authenticated]), SimpleUser(username)



class JWTAuthMiddleware(AuthenticationBackend):
    async def authenticate(self, request):
        if 'Authorization' not in request.headers:
            return

        auth = request.headers['Authorization']
        scheme, credentials = auth.split()

        if scheme.lower() != 'bearer':
            return

        try:
            payload = jwt.decode(credentials, str(settings.AUTH_KEY), algorithms=settings.AUTH_METHOD)
        except jwt.InvalidTokenError as e:
            return

        user_id = payload.get('sub')
        user = await get_user(user_id)

        if not user:
            return

        return AuthCredentials([AuthenticationScopes.authenticated]), user
