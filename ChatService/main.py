from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from chat.route import router as chat_router

app = FastAPI(title="Chat Service API", description="MSA 구성 예제 구성", version="1.0.0")

# Register routers
app.include_router(chat_router, prefix="/chat", tags=["Chat"])

@app.get("/", include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse(url='/docs')