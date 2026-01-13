from dataclasses import dataclass
from math import sqrt
from posixpath import split
from typing import Dict, List, Tuple
from algoritmo_prim import algoritmo_prim_heap
from algoritmo_kruskal import algoritmo_kruskal

#Estruturas que armazenam as propriedades dos vértices e das arestas
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
    

#Classe que representa um grafo.
#Esta classe é responsável por ler e tratar os dados dos arquivo .csv, gerando um grafo com vértices e planos
#Além de também poder executar os alfgoritmos de Prim e de Kruskal
class Grafo():
    
    def __init__(self):
        
        self.vertices : List[Vertice] = []
        self.arestas : List[Aresta] = []
        # A lista de adjacência armazena a informação de quais vértices cada vértice é conectado no grafo, além do peso da aresta que os conectam
        # Utilizada no algoritmo de Prim
        self.lista_de_adjacencia: Dict[int, List[Tuple[int, float]]] = {} 
        
    def adiciona_vertice(self, id, x, y):
        
        novo_vertice = Vertice(int(id), float(x), float(y))
        self.vertices.append(novo_vertice)
        
        
    def adiciona_aresta(self, v1, v2):
        
        v1Int = int(v1)
        v2Int = int(v2)
        peso = self.calcular_peso(v1Int, v2Int)
        
        nova_aresta = Aresta(v1Int, v2Int, peso)
        
        self.arestas.append(nova_aresta)
        
    #calcula peso de uma aresta
    def calcular_peso(self, v1Int, v2Int):
        
        vertice1 = self.vertices[v1Int]
        vertice2 = self.vertices[v2Int]
        
        peso_quadrado = (vertice1.x - vertice2.x) ** 2 + (vertice1.y - vertice2.y) ** 2
        return sqrt(peso_quadrado)
    
    def cria_lista_de_adjacencia(self):
        
        self.lista_de_adjacencia = {v.id: [] for v in self.vertices}

        
        for aresta in self.arestas:
            v1 = aresta.v1
            v2 = aresta.v2
            peso = aresta.peso

            
            if v1 in self.lista_de_adjacencia:
                self.lista_de_adjacencia[v1].append((v2, peso))
            else:
                self.lista_de_adjacencia[v1] = [(v2, peso)]

            if v2 in self.lista_de_adjacencia:
                self.lista_de_adjacencia[v2].append((v1, peso))
            else:
                self.lista_de_adjacencia[v2] = [(v1, peso)]
                
            
    def adicionar_vertices_arquivo_csv(self, nomeArquivo):
        
        try:
            with open(nomeArquivo, 'r') as arq:
                # pula cabeçalho (se houver)
                linha_arquivo = arq.readline()
                self.adiciona_vertice(0,0,0)
                linha_arquivo = arq.readline()
                while linha_arquivo and linha_arquivo.strip() != "":
                    lista_de_string = linha_arquivo.strip().split(",")
                    self.adiciona_vertice(int(lista_de_string[0]), float(lista_de_string[1]), float(lista_de_string[2]))
                    linha_arquivo = arq.readline()
                    
        except FileNotFoundError:
            print("Erro: O arquivo .csv que representa vértices não foi encontrado, verifique se está na pasta grafos")
            
    def adicionar_aresta_arquivo_csv(self, nomeArquivo):
        
        try:
            with open(nomeArquivo, 'r') as arq:
                arq.readline()
                linha_arquivo = arq.readline()
                while linha_arquivo and linha_arquivo.strip() != "":
                    lista_de_string = linha_arquivo.strip().split(",")
                    self.adiciona_aresta(int(lista_de_string[0]), int(lista_de_string[1]))
                    linha_arquivo = arq.readline()
                    
        except FileNotFoundError:
            print("Erro: O arquivo .csv que representa arestas não foi encontrado, verifique se está na pasta grafos")
    
    #Chama o algoritmo Prim
    def executa_algoritmo_prim(self):
        
        custo_final, n_subgrafos, arv_gera_min = algoritmo_prim_heap(self.lista_de_adjacencia)
        return custo_final, n_subgrafos, arv_gera_min
    
    #Chama o algoritmo Kruskal
    def executa_algoritmo_kruskal(self):
        
        custo_final, n_subgrafos, arv_gera_min = algoritmo_kruskal(self.vertices, self.arestas)
        return custo_final, n_subgrafos, arv_gera_min
    
            
    def imprime_vertice(self):
        for c in range(0, len(self.vertices)):
            print(self.vertices[c])
    
    def imprime_aresta(self):
        for aresta in self.arestas:
            print(aresta)
            
    def imprime_lista_adjacencia(self):
        
        for c in self.lista_de_adjacencia:
            print(self.lista_de_adjacencia[c])
        
        


