from fastapi import FastAPI

from fast.router import users, items

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])

app.include_router(
    items.router,
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)