import pytest

from apps.calc.service import OperationsService

service = OperationsService()


@pytest.mark.anyio
async def test_common_multiple_two_simple_numbers():
    assert service.get_mcm_for([2, 4]) == {'result': 4.0}


@pytest.mark.anyio
async def test_common_multiple_two_numbers():
    assert service.get_mcm_for([3, 40]) == {'result': 120}


@pytest.mark.anyio
async def test_common_multiple_many_numbers():
    assert service.get_mcm_for([3, 40, 3, 5, 6, 21, 54]) == {'result': 7560}
