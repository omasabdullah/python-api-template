import logging
from flask import Flask

from src.routes.v1 import v1

from werkzeug.exceptions import HTTPException
from src.ErrorHandler import error_handler
from src.Logging import setup_json_logging

import config


def create_app(config):
    # Create application and setup config
    app = Flask(__name__)
    app.config.from_object(config)

    # Add routes for users
    app.register_blueprint(v1, url_prefix=f'/api/{v1.name}')

    # Add generic error handling
    app.register_error_handler(HTTPException, error_handler)

    # Setting up custom logs
    setup_json_logging(app)

    return app


# Start server
if __name__ == '__main__':
    app = create_app(config.DevelopmentConfig)
    app.run(host='0.0.0.0')
