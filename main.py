import sys
from Grafo import Grafo
from time import time
import tracemalloc

'''
    Função principal do programa, executa ambos os algoritmos de PRIM e de Kruskal a partir do mesmo grafo.
    Após isto a função mostra as propriedades geradas pela execução dos dois algoritmos.
'''
def main():
    
    
    if len(sys.argv) > 3 or len(sys.argv) < 3:
        print("EXECUÇÃO INVÁLIDA")
        print("Para executar o programa deve se escrever a seguinte linha de comando no terminal: ")
        print("make run<N>")
        print("Sendo <N> o número inteiro no nome da pasta e do arquivo .csv de entrada")
        print("Caso não funcione digite: python main.py grafos/grafo<N>/Nodes<N>.csv grafos/grafo<N>/Edges<N>.csv")
        print("Sendo <N> o número inteiro no nome da pasta e do arquivo .csv de entrada")
        
    else:
        
        vertices_arq = sys.argv[1]
        arestas_arq = sys.argv[2]
        
        grafo = Grafo()
        grafo.adicionar_vertices_arquivo_csv(vertices_arq)
        grafo.adicionar_aresta_arquivo_csv(arestas_arq)
        grafo.cria_lista_de_adjacencia()
        
        inicio = time()
        tracemalloc.start()
        custo_final_prim, n_subgrafos_prim, arv_gera_min_prim = grafo.executa_algoritmo_prim()
        atual, pico_prim = tracemalloc.get_traced_memory()
        fim = time()
        tracemalloc.stop()
        tempo_prim = fim - inicio
        
        inicio = time()
        tracemalloc.start()
        custo_final_kruskal, n_subgrafos_kruskal, arv_gera_min_kruskal = grafo.executa_algoritmo_kruskal()
        atual, pico_kruskal = tracemalloc.get_traced_memory()
        fim = time()
        tracemalloc.stop()
        tempo_kruskal = fim - inicio
        
        
        
        
        
        
        print("-" * 50)
        print("Características da execução do Algoritmo de Prim utilizando heap: ")
        print(f"Peso da árvore geradora mínima: {custo_final_prim}")
        print(f"Quantidade de arestas escolhidas: {len(arv_gera_min_prim)}")
        print(f"O grafo escolhido contempla com : {n_subgrafos_prim} subgrafo(s)")
        print(f"Tempo de execução do algoritmo em segundos: {tempo_prim}")
        print(f"Pico de alocação de memória gerada pelo algoritmo: {pico_prim/1024 :.3f} KB")
        print("-" * 50)
        print("Características da execução do Algoritmo de Kruskal : ")
        print(f"Peso da árvore geradora mínima: {custo_final_kruskal}")
        print(f"Quantidade de arestas escolhidas: {len(arv_gera_min_kruskal)}")
        print(f"O grafo escolhido contempla com : {n_subgrafos_kruskal} subgrafo(s)")
        print(f"Tempo de execução do algoritmo em segundos: {tempo_kruskal}")
        print(f"Pico de alocação de memória gerada pelo algoritmo: {pico_kruskal/1024 :.3f} KB")
        print("-" * 50)
        
        print("Mostrando as arestas das árvores geradoras mínimas em arquivo na pasta output: ")
        
        with open('output/prim' + vertices_arq[-5], 'w') as arq1:
            
            arq1.writelines("V1  ,  V2  ,  Peso  \n")
            for c in arv_gera_min_prim:
                
                arq1.writelines(f"{c.v1}, {c.v2}, {c.peso} \n")

        with open("output/kruskal" + vertices_arq[-5], 'w') as arq2:
            
            arq2.writelines("V1  ,  V2  ,  Peso  \n")
            for c in arv_gera_min_prim:
                
                arq2.writelines(f"{c.v1}, {c.v2}, {c.peso} \n")

if __name__ == "__main__":
    main()
    