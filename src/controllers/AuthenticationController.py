import hashlib
import os
import hmac

from starlette.responses import JSONResponse

from src.ErrorHandler import Error, ErrorType
from src.database.db_mongo import users_collection
from src import strings
from src.controllers.UserController import get_users
from src.models.User import User


async def register(request):
    try:
        payload = await request.json()
    except:
        raise Error(ErrorType.generic, strings.NO_JSON_PAYLOAD)

    email = payload.get('email')
    username = payload.get('username')
    password = payload.get('password')

    if not all([email, username, password]):
        raise Error(ErrorType.generic, strings.INVALID_PAYLOAD)

    # Verify that an account with the specified email does not already exist
    filter = {'email': email}
    users = await get_users(filter=filter)

    if len(users) > 0:
        raise Error(ErrorType.generic, strings.ACCOUNT_CREATE_EXISTS)

    # Hash + Salt using pbkdf2_hmac, a slower hashing method to increase difficulty of brute forcing
    hashed_password, salt = await hash_password(
        plain_password=password
    )

    # Create account
    users_collection.insert_one({
        'email': email,
        'username': username,
        'password': hashed_password,
        'salt': salt
    })

    return JSONResponse(content={}, status_code=201)


async def login(request):
    try:
        payload = await request.json()
    except:
        raise Error(ErrorType.unauthorized, strings.LOGIN_FAILED)

    email = payload.get('email')
    password = payload.get('password')

    if not all([email, password]):
        raise Error(ErrorType.unauthorized, strings.LOGIN_FAILED)

    # Find user with email
    filter = {'email': email}
    users = await get_users(filter=filter)

    if len(users) != 1:
        raise Error(ErrorType.unauthorized, strings.LOGIN_FAILED)

    user = users[0]
    if not await verify_password(
        plain_password=password,
        salt=user.salt,
        hashed_password=user.password
    ):
       raise Error(ErrorType.unauthorized, strings.LOGIN_FAILED)

    return JSONResponse({})


async def logout(request):
    return JSONResponse()


async def hash_password(plain_password) -> (str, bytes):
    salt = os.urandom(32)

    # Use pbkdf2_hmac, a slower hashing method to increase difficulty of brute forcing
    hashed_password = hashlib.pbkdf2_hmac(
        hash_name='sha256',
        password=plain_password.encode(),
        salt=salt,
        iterations=10000,
        dklen=128
    )
    return hashed_password, salt

async def verify_password(plain_password, salt, hashed_password) -> bool:
    return hmac.compare_digest(
        hashlib.pbkdf2_hmac(
            hash_name='sha256',
            password=plain_password.encode(),
            salt=salt,
            iterations=10000,
            dklen=128
        ),
        hashed_password
    )
