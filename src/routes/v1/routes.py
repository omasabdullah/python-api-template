from src.routes import common
from src.controllers import UserController
from flask import Blueprint

api_v1 = Blueprint('api_v1', __name__)

api_v1.add_url_rule('/login', 'login', common.login, methods=['POST'])
api_v1.add_url_rule('/register', 'register', common.register, methods=['POST'])

api_v1.add_url_rule('/users', 'show', UserController.show)
api_v1.add_url_rule('/users/<int:id>', 'index', UserController.index)
api_v1.add_url_rule('/users', 'create', UserController.create, methods=['POST'])
api_v1.add_url_rule('/users/<int:id>', 'update', UserController.update, methods=['PATCH'])
