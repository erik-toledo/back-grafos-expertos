from set.infrastructure.repository.setRepository import SetRepository
from set.domain.set import Set

class UnionUseCase:
    repository:SetRepository
    def __init__(self,setRepository: SetRepository):
        self.repository = setRepository
        

    def run(self,sets:list[Set]):
        try:
           return self.repository.operations_set(set.union,sets, "Union")
        except Exception as e:
            raise e
   