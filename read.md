# Trabalho de Algoritmos em Grafos

## Aluno:
- Guilherme José Monteiro Meirelles
- RA:133994

## Instruções para execução do programa:

Dentro da pasta grafos, encontra-se alguns grafos em que cada um contempla dois arquivos: Nodes.csv e Edges.csv. O primeiro arquivo representa os nós de um grafo, com seus números de identificação e coordenadas de espaço x e y. O segundo arquivo representa as arestas de um grafo, com os dois números de cada aresta representando os identificadores dos nós que a aresta conecta. O peso de cada aresta é definido pela distância dos dois nós conectados a partir das coordenadas x e y.

Para o programa executar os algoritmos de Prim e de Kruskal a partir de um arquivo .csv de entrada. Pode-se fazer de duas maneiras
- digitar o seguinte comando no terminal: make runN

Sendo N o número inteiro correspondente ao final do nome do arquivos .csv. 
Além desta forma, pode-se digitar manualmente o seguinte comando:
- python main.py grafos/grafoN/NodesN.csv grafos/grafoN/EdgesN.csv

Sendo novamente N o número inteiro correspondente ao final do nome do arquivos .csv. Utilize sempre o mesmo valor N para todas as suas ocorrẽncias no mesmo comando de terminal.

Após os algoritmos serem executados, aparecerá no terminal os atributos dos dois algoritmos executados. Além disso, as arestas das árvores geradoras mínimas são impressas em arquivos de texto na pasta output, sendo o número no final do arquivo equivalente a N.




