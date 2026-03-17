from fastapi import FastAPI
from app.routes.analytics_routes import router as analytics_router
import uvicorn


app = FastAPI()

app.include_router(
    router=analytics_router
)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)