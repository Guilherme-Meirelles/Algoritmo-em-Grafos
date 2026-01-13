PYTHON = python3
SCRIPT = main.py

run1:
	$(PYTHON) $(SCRIPT) grafos/grafo1/Nodes1.csv grafos/grafo1/Edges1.csv

run2:
	$(PYTHON) $(SCRIPT) grafos/grafo2/Nodes2.csv grafos/grafo2/Edges2.csv

run3:
	$(PYTHON) $(SCRIPT) grafos/grafo3/Nodes3.csv grafos/grafo3/Edges3.csv

run4:
	$(PYTHON) $(SCRIPT) grafos/grafo4/Nodes4.csv grafos/grafo4/Edges4.csv

run5:
	$(PYTHON) $(SCRIPT) grafos/grafo5/Nodes5.csv grafos/grafo5/Edges5.csv

run6:
	$(PYTHON) $(SCRIPT) grafos/grafo6/Nodes6.csv grafos/grafo5/Edges6.csv
