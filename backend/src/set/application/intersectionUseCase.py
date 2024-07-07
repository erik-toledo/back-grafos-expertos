from set.infrastructure.repository.setRepository import SetRepository
from set.domain.set import Set

class IntersectionUseCase:
    repository:SetRepository
    def __init__(self,setRepository: SetRepository):
        self.repository = setRepository
        

    def run(self,sets:list[Set]):
        try:
           return self.repository.operations_set(set.intersection,sets,"Intersection")
        except Exception as e:
            raise e