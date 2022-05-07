# Programa Python para imprimir a travessia DFS 
# de um determinado grafo
from collections import defaultdict
  
# Esta classe representa um gráfico direcionado usando a 
# representação da lista de adjacências
class Graph:
  
    def __init__(self,vertices):
  
        # Numeros de vertices
        self.V = vertices
  
        # armazenamento gráfico
        self.graph = defaultdict(list)
  
    # função para adicionar uma aresta ao gráfico
    def addEdge(self,u,v):
        self.graph[u].append(v)
  
    # Uma função para realizar uma pesquisa limitada 
    # em profundidade a partir de uma determinada fonte 'src'
    def DLS(self,src,target,maxDepth):
  
        if src == target : return True
  
        # Se atingir a profundidade máxima, retorna false.
        if maxDepth <= 0 : return False
  
        # Recorrer para todos os vértices adjacentes a este vértice
        for i in self.graph[src]:
                if(self.DLS(i,target,maxDepth-1)):
                    return True
        return False
  
    # IDDFS para pesquisar se o destino for alcançável a partir de v.
    # Ele usa DLS recursivo ()
    def IDDFS(self,src, target, maxDepth):
  
        # Pesquisa repetidamente com limite de profundidade 
        # até a profundidade máxima
        for i in range(maxDepth):
            if (self.DLS(src, target, i)):
                return True
        return False
  
# Crie um gráfico dado no diagrama acima
g = Graph (7);
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 5)
g.addEdge(2, 6)
  
target = 6; maxDepth = 3; src = 0
  
if g.IDDFS(src, target, maxDepth) == True:
    print ("O alvo é alcançável a partir da origem " +
    "dentro da profundidade máxima")
else :
    print ("O destino NÃO é alcançável a partir da origem" + 
    "dentro da profundidade máxima")