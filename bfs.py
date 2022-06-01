# Busca bidirecional.
# Definição de classe para nó para ser adicionado ao gráfico
class AdjacentNode:

    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None
 
# Implementação de pesquisa bidirecional
class BidirectionalSearch:

    def __init__(self, vertices):

        # Inicialize vértices e faça um gráfico com vértices
        self.vertices = vertices
        self.graph = [None] * self.vertices
         
        # Inicializando a fila para pesquisa para frente e para trás
        self.src_queue = list()
        self.dest_queue = list()
         
        # Inicializando os nós visitados de origem e destino como False
        self.src_visited = [False] * self.vertices
        self.dest_visited = [False] * self.vertices
         
        # Inicializando nós pai de origem e destino
        self.src_parent = [None] * self.vertices
        self.dest_parent = [None] * self.vertices
         
    # Função para adicionar borda não direcionada
    def add_edge(self, src, dest): 
        # Adicionar arestas ao gráfico
         
        # Adicionar origem ao destino
        node = AdjacentNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node
 
        # Como o gráfico não é direcionado, adicione destino à origem
        node = AdjacentNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node
         
    # Função para busca em largura
    def bfs(self, direction = 'forward'):
        if direction == 'forward':
             
            # BFS na direção para frente
            current = self.src_queue.pop(0)
            connected_node = self.graph[current]
             
            while connected_node:
                vertex = connected_node.vertex
                 
                if not self.src_visited[vertex]:
                    self.src_queue.append(vertex)
                    self.src_visited[vertex] = True
                    self.src_parent[vertex] = current
                     
                connected_node = connected_node.next
        else:
             
            # BFS na direção para trás
            current = self.dest_queue.pop(0)
            connected_node = self.graph[current]
             
            while connected_node:
                vertex = connected_node.vertex
                 
                if not self.dest_visited[vertex]:
                    self.dest_queue.append(vertex)
                    self.dest_visited[vertex] = True
                    self.dest_parent[vertex] = current
                     
                connected_node = connected_node.next
                 
    # Verifique se há vértice de interseção
    def is_intersecting(self):
         
        # Retorna o nó de interseção se presente, senão -1
        for i in range(self.vertices):
            if (self.src_visited[i] and
                self.dest_visited[i]):
                return i
                 
        return -1
 
    # Imprima o caminho da origem ao destino
    def print_path(self, intersecting_node,
                   src, dest):
                        
        # Imprima o caminho final da origem ao destino
        path = list()
        path.append(intersecting_node)
        i = intersecting_node
         
        while i != src:
            path.append(self.src_parent[i])
            i = self.src_parent[i]
             
        path = path[::-1]
        i = intersecting_node
         
        while i != dest:
            path.append(self.dest_parent[i])
            i = self.dest_parent[i]
             
        print("*****Path*****")
        path = list(map(str, path))
         
        print(' '.join(path))
     
    # Função para busca bidirecional
    def bidirectional_search(self, src, dest):
         
        # Adicione a origem à fila e marque visitado 
        # como True e adicione seu pai como -1
        self.src_queue.append(src)
        self.src_visited[src] = True
        self.src_parent[src] = -1
         
        # Adicione o destino à fila e marque visitado
        # como True e adicione seu pai como -1
        self.dest_queue.append(dest)
        self.dest_visited[dest] = True
        self.dest_parent[dest] = -1
 
        while self.src_queue and self.dest_queue:
             
            # BFS na direção direta do vértice de origem
            self.bfs(direction = 'forward')
             
            # BFS na direção reversa do vértice de destino
            self.bfs(direction = 'backward')
             
            # Verifique se há vértice de interseção
            intersecting_node = self.is_intersecting()
             
            # Se existir um vértice de interseção, o caminho 
            # da origem ao destino existe
            if intersecting_node != -1:
                print(f" \nExiste um caminho entre {src} e {dest}")
                print(f"Cruzamento em : {intersecting_node}")
                self.print_path(intersecting_node,
                                src, dest)
                exit(0)
        return -1
 
if __name__ == '__main__':
    # Número de vértices no gráfico
    n = 15
     
    # Vértice de origem
    src = 0
     
    # Vértice de destino
    dest = 14
     
    # Criar um gráfico
    graph = BidirectionalSearch(n)
    graph.add_edge(0, 4)
    graph.add_edge(1, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 5)
    graph.add_edge(4, 6)
    graph.add_edge(5, 6)
    graph.add_edge(6, 7)
    graph.add_edge(7, 8)
    graph.add_edge(8, 9)
    graph.add_edge(8, 10)
    graph.add_edge(9, 11)
    graph.add_edge(9, 12)
    graph.add_edge(10, 13)
    graph.add_edge(10, 14)
     
    out = graph.bidirectional_search(src, dest)
     
    if out == -1:
        print(f"O caminho não existe entre {src} e {dest}")