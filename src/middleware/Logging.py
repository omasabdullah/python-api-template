import time
import logging
import datetime

from starlette.middleware.base import BaseHTTPMiddleware


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start_time = time.time()
        response = await call_next(request)

        end_time = time.time()
        duration = round((end_time - start_time) * 1000, 2)
        # RFC 3339
        dt = datetime.datetime.fromtimestamp(end_time)
        timestamp = dt.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

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
