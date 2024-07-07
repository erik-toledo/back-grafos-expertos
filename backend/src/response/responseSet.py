from io import BytesIO
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from set.domain.set import Set

class ResponseSet(BaseModel):
    union:list[Set]
    intersection:list[Set]
    difference:list[Set]
    symetric_difference:list[Set]
    complement:list[Set]
    image: str

    def createResponse(self):
        return{
            'union':[union.toJson() for union in self.union],
            "intersection":[intersection.toJson() for intersection in self.intersection] ,
            "difference":[difference.toJson() for difference in self.difference],
            "symetric_difference":[symetric_difference.toJson() for symetric_difference in  self.symetric_difference],
            "complement":[complement.toJson() for complement in self.complement],
            "image": self.image
        }