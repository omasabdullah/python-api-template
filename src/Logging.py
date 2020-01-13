import time
import logging

from starlette.middleware.base import BaseHTTPMiddleware

from datetime import datetime

from rfc3339 import rfc3339


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start_time = time.time()
        response = await call_next(request)

        end_time = time.time()
        duration = round((end_time - start_time) * 1000, 2)
        dt = datetime.fromtimestamp(end_time)
        timestamp = rfc3339(dt, utc=True)

        path_split = request.scope['path'].split('/')[1:]
        version = path_split[1] if len(path_split) > 2 else None

        log_params = {
            'method': request.method,
            'path': request.scope['path'],
            'status': response.status_code,
            'duration': duration,
            'timestamp': timestamp,
            'version': version,
            'ip': request.client.host,
            'host': request.scope['server'][0],
            'params': str(request.query_params)
        }

        logging.info(log_params)
        return response
