from starlette.responses import JSONResponse

from src.ErrorHandler import Error, ErrorType
from src.database.database import users


async def index(request):
    return JSONResponse(users)

async def show(request):
    id = request.path_params['user_id']

    user = await get_user(id)

    if user:
        return JSONResponse(user)
    else:
        raise Error(ErrorType.not_found, 'User not found')

async def create(request):
    new_user = await request.json()

    if new_user:
        users.append(new_user)
        return JSONResponse(content=new_user, status_code=201)
    else:
        raise Error(ErrorType.generic, 'Error creating user')

async def update(request):
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
