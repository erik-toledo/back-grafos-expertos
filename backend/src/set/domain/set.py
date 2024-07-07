import json
from pydantic import BaseModel
class Set(BaseModel):
    name:str
    set:str
    operation_set: str | None = None
    name_sets_operation: str | None = None
    name_operation: str | None = None
    result_operation:list[str]  | None = None
    region:str | None = None 
    len_operation: int | None = None


    def toJson(self):
        return {
            "name_operation":self.name_operation if self.name_operation is not None else None, 
            'name_set':self.name,
            'set':self.set, 
            "name_sets_operation":self.name_sets_operation if self.name_sets_operation is not None else None,
            "operation_set": self.operation_set if self.operation_set is not None else None,
            "result_operation": ','.join(self.result_operation ) if self.result_operation is not None else None,
        }
