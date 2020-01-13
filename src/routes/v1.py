from src.controllers import HealthController, UserController
from starlette.routing import Route, Mount

routes = []

routes.append(Route('/health', endpoint=HealthController.show))
routes.append(Route('/users', endpoint=UserController.index))
routes.append(Route('/users', endpoint=UserController.create, methods=['POST']))
routes.append(Route('/users/{user_id:int}', endpoint=UserController.show))
routes.append(Route('/users/{user_id:int}', endpoint=UserController.update, methods=['PUT']))

v1 = Mount('/api/v1', routes=[r for r in routes])
