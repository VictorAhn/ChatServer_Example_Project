from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from chat.routes import router as chat_router

app = FastAPI(title="Chat Service API", description="MSA 구성 예제 구성", version="1.0.0", root_path="/chat_service", docs_url="/docs", openapi_url="/openapi.json")

# Register routers
app.include_router(chat_router, prefix="/chat", tags=["Chat"])

@app.get("/", include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse(url='/docs')