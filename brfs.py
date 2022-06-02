
# Busca em profundidade
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

# Lista de nós visitados
visited = []
# Cria a fila
queue = []

# Funcao BrFS
def bfs(visited, graph, node):
  # Adiciona o nó na lista de visitados
  visited.append(node)
  # Adiciona o nó na fila
  queue.append(node)

  # Visita cada um dos nós
  while queue:
    # Pega o primeiro nó da lista
    m = queue.pop(0)
    # Exibe o nó
    print (m, end = " ")

    # Para cada vizinho desse nó
    for neighbour in graph[m]:
      # Se o vizinho ainda nao tiver sido visitado
      if neighbour not in visited:
        # Coloca o nó na lista de visitados
        visited.append(neighbour)
        queue.append(neighbour)

# Testando
print("A seguir está a pesquisa em largura")
bfs(visited, graph, '5')    # function calling

