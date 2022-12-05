from fastapi import APIRouter

router = APIRouter(prefix="/jokes", tags=["Jokes"])


@router.get("")
async def get_joke():
    return ""


@router.post("")
async def add_joke():
    return ""


@router.patch("")
async def update_joke():
    return ""


@router.delete("")
async def delete_joke():
    return ""
