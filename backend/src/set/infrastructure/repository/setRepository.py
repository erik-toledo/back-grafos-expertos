from copy import copy
from io import BytesIO
import itertools

from set.domain.set import Set
from matplotlib_venn import venn3_unweighted,venn2_unweighted
import matplotlib.pyplot as plt
from resources.operationsSet import OperationsSet

class SetRepository:
    def vennDiagram(sets:list[Set], intersection:list[Set]):
        labels = {}
        list_sets:list[Set] = sets + intersection
        try:
            length_set = len(sets)
            length_list_set = len(list_sets)
            combinations_regions_venn = list(itertools.product([0,1], repeat= length_set))
            combinations_regions_venn.pop(0)
            for i, combinations in enumerate(combinations_regions_venn):
                label = ''.join(map(str,combinations))
                labels[label] = ', '.join([f"Conjunto {i + 1}" for _,bit in enumerate(combinations) if bit == 1])
            sorted_labels =dict(sorted(labels.items(), key=lambda x: len(x[1]), reverse=False))  
        
            for i,key in enumerate(sorted_labels):
                if i < length_list_set:
                    list_sets[i].region = key
        
            sets_transform:list[set]= [set(item.set.split(',')) for item in sets]
            first_sorted:list[Set] = sorted(list_sets[:len(sets)], key=lambda obj: obj.region,reverse= True)
            venn_sets_labels = [_set.name for _set in first_sorted]   
            
            if(len(sets) < 4):
                venn_diagram = venn2_unweighted(sets_transform,set_labels= venn_sets_labels) if(len(sets)==2) else venn3_unweighted(sets_transform,set_labels= venn_sets_labels)
                for _set in first_sorted:
                    venn_diagram.get_label_by_id(_set.region).set_text(_set.set)
                for _set in list_sets[len(sets):]:
                    venn_diagram.get_label_by_id(_set.region).set_text(','.join(_set.result_operation))
            img_buffer = BytesIO()   
            plt.savefig(img_buffer,format='png')
            img_buffer.seek(0)
            plt.close()
            return img_buffer
        except Exception as e:
            raise ValueError(f"Error creando el Diagrama de Venn: {e}")
            
        
                    

    def operations_set(funcion,sets:list[Set],name_operation): 
        operation_symbol = OperationsSet.operations.get(name_operation)
        results:list[Set] = []
        operation = set()
        name:str = ""
        operation_set:str = ""
        try:
            
            for combo in range(2, len(sets) + 1):
                for subset in itertools.combinations(sets, combo):
                # Realizar la operación en el subconjunto actual
                    operation = set(subset[0].set.split(','))
                    name = subset[0].name
                    len_operation = len(subset)
                    for i_set in subset[1:]:
                        set_in_bucle = set(i_set.set.split(','))
                        operation = funcion(operation, set_in_bucle)
                        operation_set += f"{i_set.set} - "
                        result_sorted = sorted(list(operation))
                        name += f" {operation_symbol} {i_set.name}"
                   
                    
                    obj_set:Set = Set(name=subset[0].name, set=subset[0].set, operation_set=operation_set, name_operation=name_operation, name_sets_operation=name, result_operation=result_sorted,len_operation=len_operation)
                    exist = any(result_in_for.result_operation == result_sorted and result_in_for.len_operation == len_operation for result_in_for in results)
                    operation_set = ""
                    if  obj_set.result_operation == [] or not exist:
                        results.append(obj_set)
            return results
        except Exception as e:
            raise ValueError(f"Error en la operacion {name_operation}:{e}")

    # Realiza en complemto de cada conjunto 
    def complement(sets:list[Set],name_operation): 
        try:
            universe = set()
            results:list[Set]= []
            operation_symbol = OperationsSet.operations.get(name_operation)
            for _set in sets:
                universe |= set(_set.set.split(','))
            str_universe = ','.join(sorted(list(universe)))
            for _set in sets:
                complement = universe.difference(set(_set.set.split(',')))
                complement_sorted = sorted(list(complement))
                
                name = f"{str_universe} {operation_symbol} {_set.set}"
                obj_set = Set(name=_set.name,set=_set.set,operation_set=str_universe,name_operation=name_operation,name_sets_operation=name,result_operation=complement_sorted)
                results.append(obj_set)
            return results
        except Exception as e:
            raise ValueError(f"Error en el Complemento {e}")



            

            
