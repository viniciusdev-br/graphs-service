from itertools import product
from collections import defaultdict
import numpy as np
import random
import heapq

class AdjacencyList(object):
    def __init__(self, size):
        self._data = defaultdict(list)
        self.size = size
        self.size_org = size
        self.pathWeight = []
        self.pathNoWeighted = []
        self.Time = 0
        self.Fortes = []

    def conectar(self, nodo_origem, nodo_destino):
        self._data[nodo_origem].append(nodo_destino)

    def remover(self, nodo_origem, nodo_destino):
        self._data[nodo_origem].remove(nodo_destino)


    def fillOrder(self,v,visited, stack):
        visited[v]= True
        for i in self._data[v]:
            if visited[i]==False:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)

    def getTranspose(self):
        g = AdjacencyList(self.size)
        for i in self._data:
            for j in self._data[i]:
                g.conectar(j,i)
        return g

    def DFSUtil(self,v,visited):
        visited[v]= True
        self.Fortes.append(chr(v + 65))
        print(self.Fortes)
        print('- --',chr(v + 65))
        for i in self._data[v]:
            if visited[i]==False:
                self.DFSUtil(i,visited)

    def printSCCs(self):
        stack = []
        visited =[False]*(self.size)
        for i in range(self.size):
            if visited[i]==False:
                self.fillOrder(i, visited, stack)
        gr = self.getTranspose()
        visited =[False]*(self.size)
        while stack:
            i = stack.pop()
            if visited[i]==False:
                gr.DFSUtil(i, visited)
                print("")
                gr.Fortes.append(" - ")

        print('Componentes: ', gr.Fortes)
        self.Fortes = gr.Fortes
        return 'OI'

    def vizinhos(self, nodo):
        return self._data[nodo]
  
    def isBCUtil(self,u, visited, parent, low, disc):
        children = 0

        visited[u] = True
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1

        for v in self._data[u]:
            if visited[v] == False:
                parent[v] = u
                children += 1

                if self.isBCUtil(v, visited, parent, low, disc):
                    return True

                low[u] = min(low[u], low[v])

                if parent[u] != -1 and low[v] >= disc[u]:
                    return True
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
        return False

    def isBC(self):
        visited = [False] * (self.size)
        disc = [float("Inf")] * (self.size)
        low = [float("Inf")] * (self.size)
        parent = [-1] * (self.size)

        if self.isBCUtil(0, visited, parent, low, disc):
            return False

        if any(i == False for i in visited):
            return False

        return True



    def isReachable(self, s, d):
        visited =[False]*(self.size)


        queue=[]
  

        queue.append(s)
        visited[s] = True
  
        while queue:
 

            n = queue.pop(0)
             

            if n == d:
                return True
 
            for i in self._data[n]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

        return False  

    def tem_ciclo(self):
        # Lista dos tempos de descoberta de cada vértice
        d = [-1] * self.size
        # Lista dos tempos de finalização de cada vértice
        f = [-1] * self.size

        for vertice in range(self.size):
            if d[vertice] == -1:  # se o vértice ainda não foi visitado
                if self.tem_arco_de_retorno(vertice, d, f):
                    return True
        return False

    def tem_arco_de_retorno(self, u, d, f):
        d[u] = self.Time
        self.Time += 1

        for w in self._data[u]:
            if d[w] == -1:
                if self.tem_arco_de_retorno(w, d, f):
                    return True
            elif f[w] == -1:
                return True

        f[u] = self.Time
        self.Time += 1
        return False

    def verificar_ciclos(self, nodo_inicial):
        nodos_visitados = set()
        nodos_restantes = [nodo_inicial]
        while nodos_restantes:
            print('pláaaaaaa')
            nodo_atual = nodos_restantes.pop()
            nodos_visitados.add(nodo_atual)
            for vizinho in self.vizinhos(nodo_atual):
                if vizinho in nodos_visitados:
                    return True
                nodos_restantes.append(vizinho)
        return False

    def visita(self, vertice, d, f, ordem_topologica):
        d[vertice] = self.Time
        self.Time += 1

        for w in self._data[vertice]:
            if d[w] == -1:
                self.visita(w, d, f, ordem_topologica)

        f[vertice] = self.Time
        self.Time += 1
        ordem_topologica.append(vertice)

    def ordenacao_topologica(self):
        if self.tem_ciclo():  # Se o grafo contém ciclo, nenhuma ordenação topológica é possivel
            return []

        d = [-1] * self.size  # Tempo de descoberta
        f = [-1] * self.size  # Tempo de finalização
        ordem_topologica = []
        self.Time = 0

        for vertice in range(self.size):
            if d[vertice] == -1:  # se o vértice ainda não foi visitado
                self.visita(vertice, d, f, ordem_topologica)

        return list(reversed(ordem_topologica))

    def RF011Noweighted(self, src, dest):
        visited =[False]*(self.size)
        parent =[-1]*(self.size)
        queue=[]
        queue.append(src)
        visited[src] = True
  
        while queue :
             
            s = queue.pop(0)
             
            if s == dest:
                print("================================================", self._data)
                return self.printPath(parent, s)
                 
            for i in self._data[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    parent[i] = s     

    def printPath(self, parent, j):
        Path_len = 1
        if parent[j] == -1 and j < self.size_org : 
            self.pathNoWeighted.append(j)
            print(j),
            return 0 
        l = self.printPath(parent , parent[j])

        Path_len = l + Path_len

        if j < self.size_org :
            self.pathNoWeighted.append(j)
            print(j),
 
        return Path_len           

    def RF011Weighted(self, edges, source, sink):
        graph = [[] for n in range(self.size)]
        for p, r, c in edges:
            graph[p].append((c,r))
        queue, visited = [(0, source, [])], set()
        heapq.heapify(queue)
        while queue:
            (cost, node, path) = heapq.heappop(queue)
            if node not in visited:
                visited.add(node)
                path = path + [node]
                if node == sink:
                    return path
                for c, neighbour in graph[node]:
                    if neighbour not in visited:
                        heapq.heappush(queue, (cost+c, neighbour, path))
        return path

    def RF012(self,graph): # gera uma árvore geradora mínima
        AGM = AdjacencyList(graph.size)
        weights = []
        removed = []
        added = []
        for i in graph.edges:
            weights.append(i.weight)
        counter = 0

        while True:
            if graph.weighted == True:
                value = min(weights)
                for i in graph.edges :
                    if i.weight  == value and {i.start ,i.end ,i.weight } not in removed and {i.start ,i.end ,i.weight } not in added:
                        AGM.conectar(i.start ,i.end )
                        weights.remove(value)
                        teste_ciclo = AGM.tem_ciclo()
                        print('Tem ciclo nessa merda: ', AGM._data)
                        if teste_ciclo == True:
                            removed.append([i.start ,i.end ,i.weight ])
                            AGM.remover(i.start ,i.end )
                        else:
                            added.append([i.start ,i.end ,i.weight ])
            else:
                #weights.pop(counter)
                edge = graph.edges[counter]
                counter +=1
                AGM.conectar(edge.start ,edge.end )
                teste_ciclo = AGM.tem_ciclo()
                print('Tem ciclo nessa merda: ', teste_ciclo)
                if teste_ciclo == True:
                    removed.append([edge.start ,edge.end ])
                    AGM.remover(edge.start ,edge.end )
                else:
                    added.append([edge.start ,edge.end ])
                print(' len we ',len(weights))
                
            if len(weights) == 0 or counter == len(weights):
                return_list = []
                for i in added:
                    if graph.weighted == True:
                        aresta = {"start":i[0],"end":i[1],"weight":i[2]}
                        return_list.append(aresta)
                    else:
                        aresta = {"start":i[0],"end":i[1],"weight":0}
                        return_list.append(aresta)
                print('-------------------------------', return_list)
                return return_list
