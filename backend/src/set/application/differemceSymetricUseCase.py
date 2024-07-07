from ast import Set
from set.infrastructure.repository.setRepository import SetRepository


class SymetricDifferenceUseCase:
    repository:SetRepository
    def __init__(self,setRepository: SetRepository):
        self.repository = setRepository
        

    def run(self,sets:list[Set]):
        try:
           return self.repository.operations_set(set.symmetric_difference,sets,"Difference Symetric")
        except Exception as e:
            raise e