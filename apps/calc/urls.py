from fastapi import APIRouter

router = APIRouter(prefix="/calc", tags=["Calc"])


@router.get("/common_multiple")
def get_common_multiple():
    return ""


@router.get("/add")
def get_add():
    return ""
