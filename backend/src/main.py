from typing import Union

from fastapi import FastAPI
from router import setRoute

app = FastAPI()
app.include_router(setRoute.setRoute)


