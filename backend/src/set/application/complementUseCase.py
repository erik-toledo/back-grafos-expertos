from set.domain.set import Set
from set.infrastructure.repository.setRepository import SetRepository


class ComplementUseCase:
    repository:SetRepository
    def __init__(self,setRepository: SetRepository):
        self.repository = setRepository
        

    def run(self,sets:list[Set]):
        try:
           return self.repository.complement(sets,"Complement")
        except Exception as e:
            raise e