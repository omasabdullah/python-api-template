from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint

from src.ErrorHandler import Error, ErrorType
from src.database.database import users


class UsersController(HTTPEndpoint):
    async def get(self, request):
        return JSONResponse(users)

    async def post(self, request):
        new_user = await request.json()

        if new_user:
            users.append(new_user)
            return JSONResponse(content=new_user, status_code=201)
        else:
            raise Error(ErrorType.generic, 'Error creating user')


class UserController(HTTPEndpoint):
    async def get(self, request):
        id = request.path_params['user_id']

        user = await get_user(id)

        if user:
            return JSONResponse(user)
        else:
            raise Error(ErrorType.not_found, 'User not found')

    async def put(self, request):
        id = request.path_params['user_id']
        json = await request.json()
        user = await get_user(id)

        if user:
            user.update(json)
            return JSONResponse(user)
        else:
            raise Error(ErrorType.generic, 'Error updating user')


async def get_user(id):
    return next(
        filter(
            lambda x: x.get('id') == id,
            users
        ),
    None)
