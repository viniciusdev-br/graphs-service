import types
def extractMax(lista):
    m = lista.index(max(lista))
    lista[m] = 0
    return m


class Grafo:
    def __init__(self, arestas, orientado=True):
        self.arestas = arestas
        self.vertices = self.setVertices(arestas)
        self.numVertices = len(self.vertices)
        self.lista_adjacente = [[] for n in range(self.numVertices)]
        self.lista_adjacente_transposta = [[] for n in range(self.numVertices)]
        self.orientado = orientado
        self.ciclo = False
        self.lista_ciclos = []

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
            self.lista_adjacente_transposta[w].append(u)
            self.lista_adjacente_transposta[w].sort()
            return

        if w not in self.lista_adjacente[u]:
            self.lista_adjacente[u].append(w)
            self.lista_adjacente[u].sort()

        if u not in self.lista_adjacente[w]:
            self.lista_adjacente[w].append(u)
            self.lista_adjacente[w].sort()

    def printListaAdj(self):
        result = []
        for i in range(len(self.lista_adjacente)):
            print(f"{self.vertices[i]}: {', '.join(str(self.vertices[x]) for x in self.lista_adjacente[i])}")
            result.append(''+self.vertices[i]+': ' + ', '.join(str(self.vertices[x]) for x in self.lista_adjacente[i]))
        return str(result)

    def printListaAdjTransposta(self):
        for i in range(len(self.lista_adjacente_transposta)):
            print(
                f"{self.vertices[i]}: {', '.join(str(self.vertices[x]) for x in self.lista_adjacente_transposta[i])}")

    def listaAdjVazia(self, u, transp=False):
        if transp:
            if len(self.lista_adjacente_transposta[u]) == 0:
                return True
            return False

        else:
            if len(self.lista_adjacente[u]) == 0:
                return True
            return False

    def primeiroListaAdj(self, v, transp=False):
        if transp:
            item = self.lista_adjacente_transposta[v][0]
            if item != None:
                return self.Aresta(v, item, None)
            return None

        else:
            item = self.lista_adjacente[v][0]
            if item != None:
                return self.Aresta(v, item, None)
            return None

    def proxAdj(self, v, prox, transp=False):
        if transp:
            if prox >= len(self.lista_adjacente_transposta[v]):
                return None

            item = self.lista_adjacente_transposta[v][prox]
            prox += 1
            return self.Aresta(v, item, None)

        else:
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
        self.branco = 0
        self.cinza = 1
        self.preto = 2
        self.d = [None]*n
        self.t = [None]*n
        self.antecessor = [None]*n
        self.grafo = grafo
        self.arestasClassificadas = []
        self.classificacaoArestas = []
        self.componentesFortes = []
        if inicio == '':
            self.inicio = 0
        else:
            self.inicio = grafo.vertices.index(inicio)

    def printClassificacaoArestas(self):
        print("================= printClassificacaoArestas =================")
        result = []
        for aresta in self.classificacaoArestas:
            result.append("" + self.grafo.vertices[aresta.v1] + "→" + self.grafo.vertices[aresta.v2] + ": " + aresta.tipo)
        for i in result:
            print(i)
        print("================= END =================")
        return result

    def printTemposVertices(self):
        for v in range(self.grafo.numVertices):
            print(
                f'{self.grafo.vertices[v]} -> ({self.d[v]} | {self.t[v]}),', end=' ')
            if self.antecessor[v] != None:
                print(f'Antecessor: {self.grafo.vertices[self.antecessor[v]]}')
            else:
                print(None)

    def printComponentesFortes(self):
        print('--------------------------------')
        print(self.componentesFortes)
        return str(self.componentesFortes)

    def printCiclo(self):
        result = []
        if not self.grafo.ciclo:
            print("Não existe ciclo neste grafo!")
            return "Não existe ciclo neste grafo!"

        result.append("Existe ciclo neste grafo!")
        result.append("Existe ciclos entres os seguintes vértices: ")
        for ciclo in self.grafo.lista_ciclos:
            result.append(f'({self.grafo.vertices[ciclo[0]]}, {self.grafo.vertices[ciclo[1]]})')
            print(f'({self.grafo.vertices[ciclo[0]]}, {self.grafo.vertices[ciclo[1]]})')
        return result

    def classificarAresta(self, cor, aresta, du, dv):
        if cor == self.branco:
            return "Árvore"
        elif cor == self.preto:
            if du < dv:
                return "Avanço"
            else:
                return "Cruzamento"
        else:
            if self.grafo.orientado:
                self.grafo.ciclo = True
                if [aresta.v2, aresta.v1] not in self.grafo.lista_ciclos:
                    self.grafo.lista_ciclos.insert(-1, [aresta.v2, aresta.v1])
                return "Retorno"
            
            if str(aresta.v2)+str(aresta.v1) not in self.arestasClassificadas:
                self.grafo.ciclo = True
                if [aresta.v2, aresta.v1] not in self.grafo.lista_ciclos:
                    self.grafo.lista_ciclos.insert(-1, [aresta.v2, aresta.v1])
                return "Retorno"

    def ordemTopologica(self):
        terminos = self.t[:]
        ordemTerminos = [self.grafo.vertices[extractMax(
            terminos)] for _ in range(len(terminos))]
        
        output = []
        for aresta in self.grafo.arestas:
            edge = types.SimpleNamespace()
            edge.start = aresta[0]
            edge.end = aresta[1]
            edge.weight = 0
            output.append(edge)
        return [output, ordemTerminos]

    def dfs(self):
        tempo = 0
        cor = [None]*self.grafo.numVertices
        for u in range(0, self.grafo.numVertices):
            cor[u] = self.branco
            self.antecessor[u] = None
        
        tempo = self.visitaDfs(self.inicio, tempo, cor)
        for u in range(self.grafo.numVertices):
            if cor[u] == self.branco:
                tempo = self.visitaDfs(u, tempo, cor)

    def dfsTransposta(self):
        terminos = self.t[:]
        ordem = [extractMax(terminos) for x in range(self.grafo.numVertices)]
        tempo = 0
        cor = [None]*self.grafo.numVertices
        for u in range(0, self.grafo.numVertices):
            cor[u] = self.branco
            self.antecessor[u] = None

        for u in ordem:
            if cor[u] == self.branco:
                self.componentesFortes.append([])
                tempo = self.visitaDfs(u, tempo, cor, True)

        self.componentesFortes = [sorted(x) for x in self.componentesFortes]

    def visitaDfs(self, u, tempo, cor, transp=False):
        tempo += 1
        cor[u] = self.cinza
        self.d[u] = tempo
        if not self.grafo.listaAdjVazia(u, transp):
            a = self.grafo.primeiroListaAdj(u, transp)
            prox = 1
            while a != None:
                v = a.v2
                if self.grafo.orientado:
                    a.tipo = self.classificarAresta(
                        cor[v], a, self.d[u], self.d[v])
                    self.classificacaoArestas.append(a)
                    if cor[v] == self.branco:
                        self.antecessor[v] = u
                        tempo = self.visitaDfs(v, tempo, cor, transp)
                    a = self.grafo.proxAdj(u, prox, transp)
                    prox += 1

                if not self.grafo.orientado:
                    a.tipo = self.classificarAresta(
                        cor[v], a, self.d[u], self.d[v])
                    if str(a.v2)+str(a.v1) not in self.arestasClassificadas:
                        self.arestasClassificadas.append(str(a.v1)+str(a.v2))
                        self.classificacaoArestas.append(a)
                    if cor[v] == self.branco:
                        self.antecessor[v] = u
                        tempo = self.visitaDfs(v, tempo, cor, transp)
                    a = self.grafo.proxAdj(u, prox, transp)
                    prox += 1

        if transp:
            self.componentesFortes[-1].append(self.grafo.vertices[u])

        tempo += 1
        cor[u] = self.preto
        self.t[u] = tempo
        return tempo


if __name__ == "__main__":
    #arestas = [['R0', 'R1'], ['R1', 'R2'], ['R2', 'R1'], ['R2', 'R3']]
    # arestas = [['A', 'B'], ['A', 'D'], ['B', 'C'], ['C', 'B'], ['C', 'E'], ['D', 'A'], ['D', 'C'], ['D', 'E']] # grafo do slide conceitos_basicos pag.28
    #arestas = [['a', 'b'], ['a', 'c'], ['a', 'd'], ['c', 'b'], ['c', 'e'], ['c', 'g'], ['d', 'a'], ['d', 'e'], ['e', 'h'], ['f', 'b'], ['g', 'd'], ['g', 'f'], ['g', 'h']]
    #arestas = [['a', 'b'], ['a', 'c'], ['a', 'd'], ['c', 'b'], ['c', 'e'], ['c', 'g'], ['d', 'e'], ['e', 'h'], ['f', 'b'], ['g', 'd'], ['g', 'f'], ['g', 'h']]
    #arestas = [['A', 'B'], ['A', 'D'], ['B', 'C'], ['C', 'B'], ['C', 'E'], ['D', 'A'], ['D', 'C'], ['D', 'E']]
    arestas = [['a', 'b'], ['b', 'c'], ['b', 'e'], ['b', 'f'], ['c', 'd'], ['c', 'g'], [
        'd', 'c'], ['d', 'h'], ['e', 'a'], ['e', 'f'], ['f', 'g'], ['g', 'f'], ['g', 'h'], ['h', 'h']]
    grafo = Grafo(arestas)

    for aresta in arestas:  # inserindo as arestas
        grafo.inserirAresta(grafo.vertices.index(aresta[0]), grafo.vertices.index(aresta[1]))

    grafo.printListaAdj()  # print lista adjacencia
    teste = DFS(grafo, 'c')
    teste.dfs()
    print()
    teste.printTemposVertices()
    print()
    teste.printClassificacaoArestas()
    print()
    grafo.printListaAdjTransposta()
    teste.dfsTransposta()
    print()
    teste.printTemposVertices()
    teste.printComponentesFortes()
    print()
    teste.ordemTopologica()
    print()
    teste.printCiclo()
