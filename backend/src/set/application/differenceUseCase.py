from set.domain.set import Set
from set.infrastructure.repository.setRepository import SetRepository


class DifferenceUseCase:

    repository:SetRepository
    def __init__(self,setRepository: SetRepository):
        self.repository = setRepository
        

    def run(self,sets:list[Set]):
        try:
           return self.repository.operations_set(set.difference,sets,"Difference")
        except Exception as e:
            raise e