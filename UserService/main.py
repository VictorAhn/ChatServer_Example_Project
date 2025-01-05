from fastapi import FastAPI, APIRouter
from fastapi.openapi.utils import get_openapi
from fastapi.responses import RedirectResponse
from auth.routes import router as auth_router
from friends.routes import router as friends_router

app = FastAPI(root_path="/user_service", docs_url="/docs", openapi_url="/openapi.json")

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="User Service API",
        version="1.0.0",
        description="MSA 구성 예제 구성",
        routes=app.routes
    )
    openapi_schema["servers"] = [
        {"url": "/user_service"}  # Path만 추가
    ]
    # servers 필드 제거
    #openapi_schema.pop("servers", None)
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# Register routers
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(friends_router, prefix="/friends", tags=["Friends"])

@app.get("/", include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse(url='/docs')