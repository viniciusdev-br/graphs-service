class Grafo:
    def __init__(self, arestas, orientado=True):
        self.vertices = self.setVertices(arestas)
        self.numVertices = len(self.vertices)
        self.lista_adjacente = [[] for n in range(self.numVertices)]
        self.orientado = orientado
    
    def setVertices(self, arestas):
      vertices = []
      for l in arestas:
        vertices.append(l[0])
        vertices.append(l[1])
      return sorted(set(vertices))

    def inserirAresta(self, u, w):
      if self.orientado:
        self.lista_adjacente[u].append(w)
        self.lista_adjacente[u].sort()
        return
      
      self.lista_adjacente[u].append(w)
      self.lista_adjacente[w].append(u)
      self.lista_adjacente[u].sort()
      self.lista_adjacente[u].sort()
        
    def printListaAdj(self):
        result = []
        for i in range(len(self.lista_adjacente)):
            print(f"{self.vertices[i]}: {', '.join(str(self.vertices[x]) for x in self.lista_adjacente[i])}")
            result.append(''+self.vertices[i]+': ' + ', '.join(str(self.vertices[x]) for x in self.lista_adjacente[i]))
            print(result)
        return result

    def listaAdjVazia(self, u):
      if len(self.lista_adjacente[u]) == 0:
        return True
      return False

    def primeiroListaAdj(self, v):
        item = self.lista_adjacente[v][0]
        if item != None:
          return self.Aresta(v, item, None)
        return None

    def proxAdj(self, v, prox):
        if prox >= len(self.lista_adjacente[v]):
          return None

        item = self.lista_adjacente[v][prox]
        prox += 1
        return self.Aresta(v, item, None)

    class Aresta:
      def __init__(self, v1, v2, peso):
        self.v1 = v1
        self.v2 = v2
        self.peso = peso
        self.tipo = None

class DFS:
  def __init__(self, grafo, inicio):
    n = grafo.numVertices
    self.inicio = grafo.vertices.index(inicio)
    self.branco = 0
    self.cinza = 1
    self.preto = 2
    self.d = [None]*n; self.t = [None]*n; self.antecessor = [None]*n
    self.grafo = grafo
    self.classificacaoArestas = []

  def printClassificacaoArestas(self):
      for aresta in self.classificacaoArestas:
        print(f"{self.grafo.vertices[aresta.v1]} → {self.grafo.vertices[aresta.v2]}: {aresta.tipo}")
  
  def printTemposVertices(self):
    for v in range(self.grafo.numVertices):
      print(f'{self.grafo.vertices[v]} -> ({self.d[v]} | {self.t[v]}),',end=' ')
      if self.antecessor[v] != None:
        print(f'Antecessor: {self.grafo.vertices[self.antecessor[v]]}')
      else: print(None)

  def dfs(self):
    tempo = 0; cor = [None]*self.grafo.numVertices
    for u in range(0,self.grafo.numVertices):
      cor[u] = self.branco; self.antecessor[u] = None
    
    tempo = self.visitaDfs(self.inicio, tempo, cor)
    for u in range(self.grafo.numVertices):
      if cor[u] == self.branco:
        tempo = self.visitaDfs(u, tempo, cor)

  def visitaDfs(self, u, tempo, cor):
    tempo+=1
    cor[u] = self.cinza; self.d[u] = tempo
    if not self.grafo.listaAdjVazia(u):
      a = self.grafo.primeiroListaAdj(u)
      prox = 1
      while a != None:
        v = a.v2
        if cor[v] == self.branco:
          a.tipo = "Árvore"
          self.antecessor[v] = u
          tempo = self.visitaDfs(v, tempo, cor)
        elif cor[v] == self.preto:
          if self.d[u] < self.d[v]:
            a.tipo = "Avanço"
          else:
            a.tipo = "Cruzamento"
        elif cor[v] == self.cinza:
          a.tipo = "Retorno"
        self.classificacaoArestas.append(a)
        a = self.grafo.proxAdj(u, prox)
        prox += 1 

    tempo+=1
    cor[u] = self.preto; self.t[u] = tempo
    return tempo


if __name__ == "__main__":
    #arestas = [['R0', 'R1'], ['R1', 'R2'], ['R2', 'R1'], ['R2', 'R3']]
    #arestas = [['A', 'B'], ['A', 'D'], ['B', 'C'], ['C', 'B'], ['C', 'E'], ['D', 'A'], ['D', 'C'], ['D', 'E']] # grafo do slide conceitos_basicos pag.28
    arestas = [['a', 'b'], ['a', 'c'], ['a', 'd'], ['c', 'b'], ['c', 'e'], ['c', 'g'], ['d', 'a'], ['d', 'e'], ['e', 'h'], ['f', 'b'], ['g', 'd'], ['g', 'f'], ['g', 'h']]
    grafo = Grafo(arestas)
    

    for aresta in arestas: #inserindo as arestas
        grafo.inserirAresta(grafo.vertices.index(aresta[0]), grafo.vertices.index(aresta[1]))
    print(grafo.lista_adjacente)
    grafo.printListaAdj() #print lista adjacencia
    teste = DFS(grafo, 'a')
    teste.dfs()
    print('\n')
    teste.printTemposVertices()
    print('\n')
    teste.printClassificacaoArestas()