from fastapi import FastAPI
from app.routes.analytics_routes import router as analytics_router
from app.routes.entity_routes import router as entity_routes
import uvicorn


app = FastAPI()

app.include_router(
    analytics_router,
    prefix="/analytics"
)
app.include_router(
    entity_routes,
    prefix="entity"
)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)