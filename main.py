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
    for i in json_edjes:
        if (i.end == "None"):
            print('Sem aresta a adicionar.')
        else:
            matriz.add_edge(i.start,i.end, obj.oriented, obj.weighted, i.weight)

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

    if (requisito == 6 ):
        maiorCaminho = 1
        for i in range(obj.size):
            for j in range(obj.size):
                if (adjacencia_lista.isReachable(i, j) and i != j):
                    matriz.adjMatrix[i][j] = 1
        return { "result": matriz.RF006()}

    if (requisito == 7):
        maiorCaminho = 1
        for i in range(obj.size):
            for j in range(obj.size):
                if (adjacencia_lista.isReachable(i, j) and i != j):
                    matriz.adjMatrix[i][j] = 1
        adjacencia_lista.printSCCs()
        return { "result": matriz.RF007()}

    if ( requisito == 8 ):
        print(adjacencia_lista._data)
        if adjacencia_lista.tem_ciclo():
            return { 'result' : 'Encontrou um ciclo'}
        else:
            return { 'result' : 'Não encontrou um ciclo'}

    if ( requisito == 9 ):
        lista = adjacencia_lista.ordenacao_topologica()
        tratado = []
        for i in lista:
            tratado.append(chr(i + 65))
        return { 'result' : tratado}

    if ( requisito == 10 ):
        grafo_planar = []
        for i in json_edjes:
            if (i.start == "None"):
                print('Sem aresta a adicionar.')
            else:
                grafo_planar.append(( ord(i.start) - 65, ord(i.end) - 65 ))

        k5 = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
        k33 = [(0,1),(0,3),(0,5),(1,2),(1,4),(2,3),(2,5),(3,4),(4,5)]

        if (matriz.solve(grafo_planar, k5, matriz.size, 5) == False & matriz.solve(grafo_planar, k33, matriz.size, 5) == False):
            print('É planar.')
        else:
            print('Não é planar.')

        print('2-conexo: ', adjacencia_lista.isBC())

        if (matriz.grauPar()):
            print('Euleriano')
            print('Caminho: ', matriz.pathEuler(len(json_edjes)))
        else: 
            print('Não euleriano')

    if ( requisito == 11):
        RF11 = Matriz(obj.size)
    # ----------------- Monta a matriz de adjacência -------------------
        for i in json_edjes:
            if (i.end == "None"):
                print('Sem aresta a adicionar.')
            else:
                RF11.add_edge(i.start,i.end, obj.oriented, obj.weighted, i.weight)
        RF11.print_matrix()
        
