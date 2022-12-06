from functools import reduce


class OperationsService:
    def mcm(self, a: int, b: int):
        if a > b:
            great_than = a
        else:
            great_than = b

        while True:
            if great_than % a == 0 and great_than % b == 0:
                mcm = great_than
                break
            great_than += 1

        return mcm

    def get_mcm_for(self, store_list: list[int]):
        mcm = reduce(lambda x, y: self.mcm(x, y), store_list)
        return {"result": mcm}
