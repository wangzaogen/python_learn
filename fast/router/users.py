from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["users"])
async def read_users():
    return {"msg":"here is users"}