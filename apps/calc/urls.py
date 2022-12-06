from fastapi import APIRouter, Query, Depends

from apps.calc.service import OperationsService

router = APIRouter(prefix="/calc", tags=["Calc"])


@router.get("/common_multiple")
def get_common_multiple(service: OperationsService = Depends(), list_numbers: list[int] = Query(...)):
    return service.get_mcm_for(list_numbers)


@router.get("/add")
def get_increase_number(number: int = Query(...)):
    return {"next": number + 1}
