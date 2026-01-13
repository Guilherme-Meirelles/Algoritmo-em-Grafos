import heapq
from typing import Dict, List, Tuple
from dataclasses import dataclass
from time import time

@dataclass
class Aresta:
    v1: int
    v2: int
    peso: float


# Algoritmo de Prim que utiliza uma função heap para armazenar vertice adjacentes e ordena-los em relação ao peso da aresta de adjacência.
def algoritmo_prim_heap(lista_adjacencia: Dict[int, List[Tuple[int, float]]]):
    
    
    peso_vertices = [float('inf')] * len(lista_adjacencia)
    pai = [0] * len(lista_adjacencia)
    vertices_inseridos = [0] * len(lista_adjacencia)
    peso_final = 0
    
    subgrafos = 0
    arvore_minima :List[Aresta] = []
    
    for i in range (1, len(lista_adjacencia)):
        
        if vertices_inseridos[i] == 1:
            continue
        
        subgrafos += 1
        
        peso_vertices[i] = 0
        
        heap: List[Tuple[float, int]] = [(0.0, i)] #heap
      
        
        while heap:
            
            peso, Uv = heapq.heappop(heap)
            
            if vertices_inseridos[Uv] == 1:
                continue
           
            if peso != peso_vertices[Uv]:
                continue
            
            vertices_inseridos[Uv] = 1
            
            if pai[Uv] != 0:
                peso_final += peso
                arvore_minima.append(Aresta(pai[Uv], Uv, peso))
               
            
            for no, peso2 in lista_adjacencia[Uv]:
                
                if vertices_inseridos[no] == 1:
                    continue
              
                if peso2 < peso_vertices[no]:
                    
                    peso_vertices[no] = peso2
                    pai[no] = Uv
                    heapq.heappush(heap, (peso2, no))
                    
              
    return peso_final, subgrafos, arvore_minima