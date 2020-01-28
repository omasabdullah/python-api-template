import base64
import binascii
import jwt

from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint

from src.ErrorHandler import Error, ErrorType
from src.controllers.AuthenticationController import authenticate_user
from src.controllers.UserController import get_user
from src import settings

from src.models.User import User

from starlette.authentication import AuthenticationBackend, AuthenticationError, SimpleUser, UnauthenticatedUser, AuthCredentials

class BasicAuthMiddleware(AuthenticationBackend):
    async def authenticate(self, request):
        if 'Authorization' not in request.headers:
            return

        auth = request.headers['Authorization']
        scheme, credentials = auth.split()
        username, password = None, None

        if scheme.lower() == 'basic':
            try:
                decoded = base64.b64decode(credentials).decode('ascii')
            except (ValueError, UnicodeDecodeError, binascii.Error) as e:
                raise AuthenticationError('Invalid basic auth')

            username, _, password = decoded.partition(':')

            if await authenticate_user(
                email=username,
                password=password
            ):
                return AuthCredentials(['authenticated']), SimpleUser(username)

        return AuthCredentials(), UnauthenticatedUser()


class JWTAuthMiddleware(AuthenticationBackend):
    async def authenticate(self, request):
        if 'Authorization' not in request.headers:
            return

        auth = request.headers['Authorization']
        scheme, credentials = auth.split()

        if scheme.lower() == 'bearer':
            try:
                payload = jwt.decode(credentials, str(settings.JWT_PUBLIC_KEY), algorithms=['RS256'])
            except jwt.InvalidTokenError as e:
                raise AuthenticationError('Invalid JWT')

            user_id = payload.get('id')
            user = await get_user(user_id)

            return AuthCredentials(payload.get('scopes', [])), user

        return AuthCredentials(), UnauthenticatedUser()
