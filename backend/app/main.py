from fastapi import FastAPI
from app.core.logger import logger, setup_logging
from app.core.database import Base, engine

setup_logging()
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    logger.info("Root endpoint called")
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    logger.info("Item endpoint called", extra={"item_id": item_id, "q": q})
    return {"item_id": item_id, "q": q}