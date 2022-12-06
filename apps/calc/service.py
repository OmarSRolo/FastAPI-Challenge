from functools import reduce


class OperationsService:
    def mcm(self, a, b):
        if a > b:
            mayor_que = a
        else:
            mayor_que = b

        while True:
            if mayor_que % a == 0 and mayor_que % b == 0:
                mcm = mayor_que
                break
            mayor_que += 1

        return mcm

    def obtener_mcm_for(self, lista_almacenada):
        mcm = reduce(lambda x, y: self.mcm(x, y), lista_almacenada)
        return {"result": mcm}
