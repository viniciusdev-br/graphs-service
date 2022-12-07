import types
from itertools import product
from collections import defaultdict
from queue import PriorityQueue
import numpy as np
import random
import heapq

class Matriz(object):

    # Initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size
        self.Visited = []

    def add_edge(self, v1, v2, oriented, weighted, weight):
        if (weighted):
            if (oriented):
                self.adjMatrix[ord(v1) - 65][ord(v2) - 65] = weight
            else:
                self.adjMatrix[ord(v1) - 65][ord(v2) - 65] = weight
                self.adjMatrix[ord(v2) - 65][ord(v1) - 65] = weight
        else: 
            if (oriented):
                self.adjMatrix[ord(v1) - 65][ord(v2) - 65] = 1
            else:
                self.adjMatrix[ord(v1) - 65][ord(v2) - 65] = 1
                self.adjMatrix[ord(v2) - 65][ord(v1) - 65] = 1


    def grauPar(self):
        graus = np.sum(self.adjMatrix, axis=1)
        for grau in graus:
            if (grau%2 == 1):
                print('Vértice com grau par encontrado')
                return False
        return True

    def pathEuler(self, numAres):
        grafo = self.size
        noInicial = 0
        print(numAres)
        path = []
        visitados = []
        while(True):
            noAtual = noInicial
            visitados.append(noInicial)
            while(True):
                for u in range(self.size):
                    if (self.adjMatrix[noAtual][u] == 1):
                        path.append([noAtual,u])
                        self.adjMatrix[noAtual][u] = -1
                        self.adjMatrix[u][noAtual] = -1
                        visitados.append(u)
                        noAtual = u
                        break;
                if (noInicial == noAtual):
                    print('noini e act')
                    break;
            if (numAres == len(path)):
                return path

            while(True):
                aux = random.randint(0, grafo-1)
                if (aux not in visitados):
                    noInicial = aux
                    break;

    def RF005(self): # teste de fracamente conexo
        order = self.size
        duplas = 0
        teste = order -1
        conections = 0

        line = 0
        for i in self.adjMatrix:
            column = 0
            for j in i:
                if j == 1 and line != column:
                    conections += 1
                column += 1
            line += 1

        while teste > 0:
            duplas += teste
            teste -= 1
        
        if duplas > conections:
            return True
        else:
            return False

        
    def RF006(self):
        graph = self.adjMatrix
        n = self.size
        strongly = True;
        for i in range(n):
            for j in range(n):
                if (graph[i][j] != graph[j][i]):
                    strongly = False;
                    break
            if not strongly:
                break;
        if (strongly):
            return False
        uppertri = True;
        for i in range(n):
            for j in range(n):
                if (i > j and graph[i][j] == 0):
                    uppertri = False;
                    break;            
            if not uppertri:
                break;
        if uppertri:
            return True
        lowertri = True;
        for i in range(n):
            for j in range(n):
                if (i < j and graph[i][j] == 0):
                    lowertri = False;
                    break;
            if not lowertri:
                break;        
        if lowertri:
            return True
        else:
            return False

    def RF007(self): # teste de fortemente conexo
        order = self.size
        fortemente_conexo = True
        line = 0

        for i in self.adjMatrix:
            column = 0
            for j in i:
                if j != 1 and line != column:
                    fortemente_conexo = False
                column += 1
            line += 1

        if fortemente_conexo == True:
            return True
            # return conjunto de elementos fortemente conexos
        else:
            return False

    def __len__(self):
        return self.size
    
    # Print the matrix
    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:4}'.format(val), end=""),
            print('\n')

    def existe_edge(self):
      for row in self.adjMatrix:
            for val in row:
                if ( val == 1):
                  return True

    def grau_edge(self, oriented, vertex):
        num_emissao = 0
        num_recepcao = 0
        num_grau = 0
        if (oriented):
            for i in range(self.size):
                if (self.adjMatrix[ord(vertex) - 65][i] != 0):
                    num_emissao = num_emissao + self.adjMatrix[ord(vertex) - 65][i]
                if (self.adjMatrix[i][ord(vertex) - 65] != 0):  
                    num_recepcao = num_recepcao +  self.adjMatrix[i][ord(vertex) - 65]
            return [num_emissao, num_recepcao]
        else:
            for i in range(self.size):
                if (self.adjMatrix[ord(vertex) - 65][i] != 0):
                    num_grau = num_grau + self.adjMatrix[ord(vertex) - 65][i]
            return num_grau

    def verify(self, G, H, f):
        homomorphism = True
        for edge in G:
            if not ((f[edge[0]], f[edge[1]]) in H):
                homomorphism = False
                break
        return homomorphism


    def solve(self, G, H, n, m):
        rangeG = [i for i in range(n)]
        assignments = list(product(rangeG, repeat=m))
        cnt = 0
      
        for f in assignments:
            if self.verify(G, H, f):
                return True
        return False

    def adjacencia_vertex(self, oriented, vertex):
        oriented_sucessor = []
        oriented_antecessor = []
        digrafo = []
        if (oriented):
            for i in range(self.size):
                if (self.adjMatrix[ord(vertex) - 65][i] != 0):
                    oriented_sucessor.append(chr(i + 65))
                if (self.adjMatrix[i][ord(vertex) - 65] != 0):  
                    oriented_antecessor.append(chr(i + 65))
            return [(oriented_sucessor), oriented_antecessor]
        else:
            for i in range(self.size):
                if (self.adjMatrix[ord(vertex) - 65][i] != 0):
                    digrafo.append(chr(i + 65))
            return digrafo 

    def dijkstra(self, start_vertex):
        graph = self.adjMatrix
        D = {v:float('inf') for v in range(graph.v)}
        D[start_vertex] = 0

        pq = PriorityQueue()
        pq.put((0, start_vertex))

        while not pq.empty():
            (dist, current_vertex) = pq.get()
            graph.visited.append(current_vertex)

            for neighbor in range(graph.v):
                if self.adjMatrix[current_vertex][neighbor] != -1:
                    distance = self.adjMatrix[current_vertex][neighbor]
                    if neighbor not in graph.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
        return D

    def is_scrappy(self, obj):
        vertices = []
        conected = []
        for i in obj.edges:
            if i.start not in vertices and i.start != "None":
                vertices.append(i.start)
            if i.end not in vertices and i.end != "None":
                vertices.append(i.end)

        for i in vertices:
            for j in obj.edges:
                if j.start  == i and j.end  != "None" and j.end  != i:
                    conected.append(j.start ) if j.start  not in conected else "None"
                    conected.append(j.end ) if j.end  not in conected else "None"
                    continue
                elif j.end  == i and j.start  != "None" and j.start  != i:
                    conected.append(j.start ) if j.start  not in conected else "None"
                    conected.append(j.end ) if j.end  not in conected else "None"
                    continue

        for i in conected:
            vertices.remove(i)
        if len(vertices) == 0:
            #return None
            return True
        else:
            #return vertices
            return False

    def minDistancia(self, dist, sptSer, tamanho):
        min = 99999999
        min_index = 0
        for v in range(tamanho):
            if (sptSer[v] == False and dist[v] <= min):
                min = dist[v]
                min_index = v
        return min_index;
    
    def dijkstra(self, graph, src, tamanho):
        dist = [999999 for n in range(tamanho)]
        sptSet = [False for n in range(tamanho)]
        dist[src] = 0
        for count in range(tamanho):
            u = self.minDistancia(dist, sptSet, tamanho)
            sptSet[u] = True
            for v in range(tamanho):
                if ((not sptSet[v]) and graph[u][v] and (dist[u] != 999999) and dist[u] + graph[u][v] < dist[v]):
                    dist[v] = dist[u] + graph[u][v]
        result = [f"Para o vértice {src} temos os respectivos pesos mínimos alcançados: "]
        print("V - D")
        for i in range(len(dist)):
            print(i,'-',dist[i])
            result.append(''+str(chr(i+65))+' - '+str(dist[i]))
        return result

    def prim(self, vizinhos,raiz):
        n = len(vizinhos)

        H = []

        print(raiz)

        for (x,c) in vizinhos[raiz]: heapq.heappush(H, (c, raiz, x)) #Adiciona os vertices adjecente à raiz
        print(H)

        aresta = 0
        custo_total = 0 
        vertices_encontradas = [raiz] #Adiciona a raiz nos vertices encontrados
        solucao = [] 

        while aresta < n-1:
            while True:
                (c,a,b) = heapq.heappop(H) 
                if b not in vertices_encontradas:
                    break
            vertices_encontradas.append(b) #adiciona uma vertice a solucao
            custo_total += c
            solucao.append((a,b))
            aresta += 1
            for (x, c) in vizinhos[b]:
                if x not in vertices_encontradas:
                    heapq.heappush(H, (c, b, x))
        print(solucao)
        print(custo_total)
        return [custo_total, str(solucao)]
        
class Req12:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = []
        self.output = ''
 
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
 
 
    def search(self, parent, i):
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])
 
    def apply_union(self, parent, rank, x, y):
        xroot = self.search(parent, x)
        yroot = self.search(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
 
  
    def kruskal(self):
        result = []
        output = list()
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.search(parent, u)
            y = self.search(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        
        for u, v, weight in result:
            edge = types.SimpleNamespace()
            edge.start = chr(u + 65)
            edge.end = chr(v + 65)
            edge.weight = weight
            output.append(edge)
        return output
#vizinhos = [[(1,6),(2,1),(3,5)], #0
#            [(0,6),(2,2),(4,5)], #1
#            [(0,1),(1,2),(3,2),(4,6),(5,5)], #2
#            [(0,5),(2,2),(5,4)], #3
#            [(1,5),(2,6),(5,3)], #4
#            [(2,4),(3,4),(4,3)]] #5

