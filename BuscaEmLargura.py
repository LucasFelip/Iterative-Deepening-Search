from collections import defaultdict
 
# Grafico Direcionado
class Grafo:
 
    # Construtor
    def _init_(self):
        # Dicionario para guardar o grafo
        self.grafo = defaultdict(list)
 
    # function to add an edge to graph
    def addVertice(self,vertOri,vertDes):
        self.grafo[vertOri].append(vertDes)
 
    # Function to print a BFS of graph
    def bfs(self, vertOri):

        # Marca todos os vertices como nao visitados
        visitados = [False] * (max(self.grafo) + 1)
			
        # Cria uma fila para usar no algoritmo
        fila = []
 
        # Marca o vertice de origem como visitado
				# E o coloca na lista
        fila.append(vertOri)
        visitados[vertOri] = True
 
        while fila:
            # Retira um vertice da fila
						# E exibe o seu valor
            s = fila.pop(0)
            print (s, end = " ")
 
            # Pega todos os vertices adjacentes do
						# vertice atual, e caso um deles nao tenha
						# sido visitado, o visita
            for i in self.grafo[s]:
                if visitados[i] == False:
                    fila.append(i)
                    visitados[i] = True
 
# Teste
grafo = Grafo()
grafo.addVertice(0, 1)
grafo.addVertice(0, 2)
grafo.addVertice(1, 2)
grafo.addVertice(2, 0)
grafo.addVertice(2, 3)
grafo.addVertice(3, 3)
grafo.addVertice(3, 1)
 
print ("Iniciando do vertice 2: ")
grafo.bfs(2)