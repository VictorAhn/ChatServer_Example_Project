from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from auth.routes import router as auth_router
from friends.routes import router as friends_router

app = FastAPI(title="User Service API", description="MSA 구성 예제 구성", version="1.0.0", docs_url="/docs", openapi_url="/user_api/openapi.json")

# Register routers
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(friends_router, prefix="/friends", tags=["Friends"])

@app.get("/", include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse(url='/docs')