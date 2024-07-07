from ast import Set
from set.infrastructure.repository.setRepository import SetRepository


class VennUseCase:
    repository:SetRepository
    def __init__(self,setRepository: SetRepository):
        self.repository = setRepository
        
    def run(self,sets:list[Set], intersection:list[Set]):
        try:
           return self.repository.vennDiagram(sets,intersection)
        except Exception as e:
            raise e