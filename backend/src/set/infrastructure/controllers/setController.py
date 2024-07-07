
from set.domain.set import Set
from set.application.unionUseCase import UnionUseCase
from set.application.intersectionUseCase import IntersectionUseCase
from set.application.differemceSymetricUseCase import SymetricDifferenceUseCase
from set.application.complementUseCase import ComplementUseCase
from set.application.differenceUseCase import DifferenceUseCase
from set.application.vennUseCase import VennUseCase
from set.infrastructure.repository.setRepository import SetRepository
class SetController:
    def operations_set_controller(sets:list[Set]):
        try:
            results_operations = []
            results_operations.append(UnionUseCase(setRepository=SetRepository).run(sets=sets))
            results_operations.append(IntersectionUseCase(setRepository=SetRepository).run(sets=sets))
            results_operations.append(DifferenceUseCase(setRepository=SetRepository).run(sets=sets))
            results_operations.append(SymetricDifferenceUseCase(setRepository=SetRepository).run(sets=sets))
            results_operations.append(ComplementUseCase(setRepository=SetRepository).run(sets=sets))
            results_operations.append(VennUseCase(setRepository=SetRepository).run(sets=sets,intersection=results_operations[1]))
            return results_operations
        except Exception as e:
            raise e