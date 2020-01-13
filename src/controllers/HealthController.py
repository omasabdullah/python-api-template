from starlette.responses import JSONResponse


async def show(request):
    return JSONResponse({})
