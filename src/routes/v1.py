from src.controllers import UserController, HealthController
from flask import Blueprint


v1 = Blueprint('v1', __name__)

v1.add_url_rule('/health', 'health', HealthController.show)

v1.add_url_rule('/users', 'users_show', UserController.show)
v1.add_url_rule('/users/<int:id>', 'users_index', UserController.index)
v1.add_url_rule('/users', 'users_create', UserController.create, methods=['POST'])
v1.add_url_rule('/users/<int:id>', 'users_update', UserController.update, methods=['PATCH'])

# v1.add_url_rule('/login', 'login', common.login, methods=['POST'])
# v1.add_url_rule('/register', 'register', common.register, methods=['POST'])
