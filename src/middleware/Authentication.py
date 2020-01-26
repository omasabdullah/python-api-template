from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint

from src.ErrorHandler import Error, ErrorType
from src.database.db_mongo import users_collection

from src.models.User import User

from starlette.authentication import AuthenticationBackend, AuthenticationError, SimpleUser, UnauthenticatedUser, AuthCredentials

import base64
import binascii

class AuthMiddleware(AuthenticationBackend):
    async def authenticate(self, request):
        if 'Authorization' not in request.headers:
            return

        auth = request.headers['Authorization']
        scheme, credentials = auth.split()
        username, password = None, None

        # Basic auth
        if scheme.lower() == 'basic':
            username, password = self.basic(credentials=credentials)

            if username == 'omas' and password == 'test':
                return AuthCredentials(['authenticated']), SimpleUser(username)

        return AuthCredentials(), UnauthenticatedUser()

    async def basic(self, credentials):
        try:
            decoded = base64.b64decode(credentials).decode('ascii')
        except (ValueError, UnicodeDecodeError, binascii.Error) as e:
            raise AuthenticationError('Invalid basic auth')

        username, _, password = decoded.partition(':')

        return username, password
