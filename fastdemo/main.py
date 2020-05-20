from fastapi import FastAPI

from fastdemo.users import read_users

app = FastAPI()

app.include_router(read_users, prefix="/users", tags=["users"])

# app.include_router(
#     items.router,
#     prefix="/items",
#     tags=["items"],
#     responses={404: {"description": "Not found"}},
# )