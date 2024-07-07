import base64
from urllib import response
from fastapi import APIRouter
from set.domain.set import Set
from set.infrastructure.controllers.setController import SetController
from response.responseSet import ResponseSet
from fastapi.responses import StreamingResponse,JSONResponse



setRoute = APIRouter()
@setRoute.post("/sets")
async def operations_set(request:list[Set]):
    try:
        # img_buffer =  SetController.operations_set_controller(request)
        
        union,intersection,difference,symetric_difference,complement,img_buffer =  SetController.operations_set_controller(request)     
        img_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
        response = ResponseSet(
            union= union,
            complement= complement,
            intersection=intersection,
            difference=difference,
            symetric_difference=symetric_difference,
            image= img_base64
        ).createResponse()
   

        return JSONResponse(status_code=200,content=response)
    except Exception as e:
        return JSONResponse(status_code=500,content={"message": f"Error {str(e)}"})