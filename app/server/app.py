from fastapi import FastAPI
from server.routes.book import router as BookRouter
from server.access import shut_db_client

MONGO_DETAILS = "mongodb://localhost:27017/"

app = FastAPI()


@app.on_event("shutdown")
def shutdown_db_client():
    shut_db_client()


app.include_router(BookRouter, tags=["Books"], prefix="/books")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to book app!"}


