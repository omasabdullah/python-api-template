from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint

class HealthController(HTTPEndpoint):
    async def get(self, request):
        return JSONResponse({})
