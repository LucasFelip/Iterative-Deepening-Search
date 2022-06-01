# Busca em profundidade
# Usando um dicionário Python para atuar como uma lista de adjacências
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() # Definição para acompanhar os nós visitados do grafo.

def dfs(visited, graph, node):  #função para dfs
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Codigo
print("A seguir está a pesquisa em profundidade: ")
dfs(visited, graph, '5')