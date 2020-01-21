from src.controllers.HealthController import HealthController
from src.controllers.UserController import UserController, UsersController
from starlette.routing import Route, Mount

routes = []

routes.append(Route('/health', endpoint=HealthController))
routes.append(Route('/users', endpoint=UsersController))
routes.append(Route('/users/{user_id:int}', endpoint=UserController))

v1 = Mount('/api/v1', routes=[r for r in routes])
