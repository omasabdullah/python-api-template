from src.controllers.HealthController import HealthController
from src.controllers.UserController import UserController, UsersController
from src.controllers.AuthenticationController import register, login, logout
from starlette.routing import Route, Mount

routes = []

routes.append(Route('/health', endpoint=HealthController))
routes.append(Route('/users', endpoint=UsersController))
routes.append(Route('/users/{user_id:str}', endpoint=UserController))

routes.append(Route('/register', endpoint=register, methods=['POST']))
routes.append(Route('/login', endpoint=login, methods=['POST']))
routes.append(Route('/logout', endpoint=logout, methods=['POST']))

v1 = Mount('/api/v1', routes=[r for r in routes])
