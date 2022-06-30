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

    json_edjes = obj.edges
    matriz = Matriz(obj.size)
    # ----------------- Monta a matriz de adjacência -------------------
    if (obj.weighted == False):
        for i in json_edjes:
            if (i.end == "None"):
                print('Sem aresta a adicionar.')
            else:
                matriz.add_edge(i.start,i.end, obj.oriented)

    requisito = obj.requirement

    # ------------------ Monta a lista de adjacência -------------------

    adjacencia_lista = AdjacencyList(obj.size)
    for i in json_edjes:
        if (i.start == "None"):
            print('Sem aresta a adicionar.')
        else:
            adjacencia_lista.conectar(ord(i.start) - 65,ord(i.end) -65)

# _________________________________________________________________

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

    if ( requisito == 2):
        matriz.print_matrix()
        return {"result" : matriz.grau_edge(obj.oriented, obj.selected_vertex)}

    if ( requisito == 3 ):
        # Caso o grafo seja orientado será retornado um vetor, o primeiro elemento são os seus sucessores, o segundo é o seu antecessor
        return {"result" : matriz.adjacencia_vertex(obj.oriented, obj.selected_vertex)}

    if ( requisito == 4 ):
        return { "result": matriz.is_scrappy(obj) }

    if ( requisito == 5 ):
        maiorCaminho = 1
        for i in range(obj.size):
            for j in range(obj.size):
                if (adjacencia_lista.isReachable(i, j) and i != j):
                    matriz.adjMatrix[i][j] = 1
        return { "result": matriz.RF005()}
