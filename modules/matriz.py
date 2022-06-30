from itertools import product
from collections import defaultdict
import numpy as np
import random

class Matriz(object):

    # Initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    def add_edge(self, v1, v2, oriented):
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
                aux = random.randint(0, len(grafo)-1)
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

        
    def RF006(self): # teste de unilateralmente conexo
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

        if duplas == conections:
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

    def is_scrappy(self, pseudoMatriz=None):
        if (pseudoMatriz == None):
            count = 0
            for row in self.adjMatrix:
                for val in row:
                    if (val == 0):
                        count += 1
                    if (count == self.size):
                        return True
                    else: 
                        count = 0
            if (count == 0):
                return False
        else:
            count = 0
            for row in pseudoMatriz:
                for val in row:
                    if (val == 0):
                        count += 1
                    if (count == self.size):
                        return True
                    else: 
                        count = 0
            if (count == 0):
                return False 
        