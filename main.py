from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models.graphs import Graph
from modules.adjacencia import AdjacencyList
from modules.matriz import Matriz

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

@app.get("/healthcheck")
def HealthCheck():
    return {"status": "OK"}

    
@app.post("/teste")
def Soma(obj : Graph):

    requisito = obj.requirement

    if ( requisito == 1):
        test = False
        if obj.oriented == True:
            for i in graph.edges:
                if i.start == start and i.end == end:
                    test = True
        else:
            for i in obj.edges:
                if i.start == obj.selected_vertex and i.end == obj.selected_vertex2 or i.start == obj.selected_vertex2 and i.end == obj.selected_vertex:
                    test = True
        return {"result": test}

    return {"result" : obj.edges, "status" : True}
        