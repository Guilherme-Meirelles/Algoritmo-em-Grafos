from dataclasses import dataclass
from typing import List


@dataclass
class Vertice: 
    id: int
    x: float
    y: float
    
@dataclass
class Aresta:
    v1: int
    v2: int
    peso: float
    
#Classe auxiliar que auxiliar na execução do algoritmmo de kruskal
class ConjuntoVertices:
    
    def __init__(self, n:int):
        
        self.pai = list(range(0, n+1))
        self.rank = [0] * (n+1)

    def busca(self, k):
        if self.pai[k] != k:
            self.pai[k] = self.busca(self.pai[k])
        return self.pai[k]

    def uniao(self, v1, v2):
        r1 = self.busca(v1)
        r2 = self.busca(v2)

        if r1 == r2:
            return False

        if self.rank[r1] < self.rank[r2]:
            self.pai[r1] = r2

        elif self.rank[r1] > self.rank[r2]:
            self.pai[r2] = r1

        else:
            self.pai[r2] = r1
            self.rank[r1] += 1

        return True
    
#Algoritmo de Kruskal, não foi necessário usar uma lista de adjacência neste algoritmo
def algoritmo_kruskal(vertices: List[Vertice], arestas: List[Aresta]):
  
    
    cv = ConjuntoVertices(len(vertices))
    arestas_sorteadas = sorted(arestas, key=lambda a: a.peso) # Weight

    arvore_minima = []
    peso_final = 0.0

    for aresta in arestas_sorteadas:
        
        if cv.uniao(aresta.v1, aresta.v2):
            arvore_minima.append((aresta.v1, aresta.v2, aresta.peso))
            peso_final += aresta.peso

            if len(arvore_minima) == len(vertices):
                break
            
    raizes = set()
    for i in range(len(vertices)):
        raizes.add(cv.busca(i))
    subgrafos = len(raizes) - 1

   
            
    return peso_final, subgrafos, arvore_minima