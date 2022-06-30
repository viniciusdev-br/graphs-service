from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models.graphs import Graph
from modules.adjacencia import AdjacencyList
from modules.matrz import Matriz

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def HomePage():
    return {"Hello": "World"}

    
@app.post("/teste")
def Soma(obj : Graph):

    requisito = obg.requirement

    if ( requisito == 1):
        test = False
        if obj.oriented == True:
            for i in graph.edges:
                if i.start == start and i.end == end:
                    test = True
        else:
            for i in graph.edges:
                if i.start == start and i.end == end or i.start == end and i.end == start:
                    test = True
        return {"result": test}

    return {"result" : obj.edges, "status" : True}
        