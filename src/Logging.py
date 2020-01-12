import json
import time
import logging

from datetime import datetime

from rfc3339 import rfc3339

from flask import request, current_app

log = logging.getLogger('werkzeug')
log.disabled = True

def setup_json_logging(flask_app):
    handler = flask_app.logger.handlers[0]
    handler.setFormatter(logging.Formatter('%(message)s'))
    flask_app.before_request_funcs.setdefault(None, []).append(before_log_request)
    flask_app.after_request_funcs.setdefault(None, []).append(after_log_request)


def before_log_request():
    request.start_time = time.time()


def after_log_request(response):
    now = time.time()
    duration = round((now - request.start_time) * 1000, 2)
    dt = datetime.fromtimestamp(now)
    timestamp = rfc3339(dt, utc=True)

    path_split = request.path.split('/')[1:]
    version = path_split[1] if len(path_split) > 2 else None

    log_params = {
        'method': request.method,
        'path': request.path,
        'status': response.status_code,
        'duration': duration,
        'timestamp': timestamp,
        'version': version,
        'ip': request.remote_addr,
        'host': request.host,
        'params': request.args,
    }

    current_app.logger.info(json.dumps(log_params))

    return response
