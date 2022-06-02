

# Retorna o menor caminho
def uniform_cost_search(goal, start):
	
	global graph,cost
	answer = []

	# Cria uma fila de prioridades
	queue = []

	# Diz que todos os caminhos sao infinitos
	for i in range(len(goal)):
		answer.append(10**8)

	# poe na fila o primeiro vertice
	queue.append([0, start])

	# guarda os nós visitados
	visited = {}
	count = 0

	# Enquanto a fila nao estiver vazia
	while (len(queue) > 0):

		# Pega o elemento no topo da fila
		queue = sorted(queue)
		p = queue[-1]

		# remove o elemento
		del queue[-1]

		# pega o valor original
		p[0] *= -1

		# verifica se o elemento faz parte do objetivo
		if (p[1] in goal):

			# pega a posicao
			index = goal.index(p[1])

			# se um novo caminho for encontrado
			# aumenta o contador
			if (answer[index] == 10**8):
				count += 1

			# se o custo eh menor, garda o custo
			if (answer[index] > p[0]):
				answer[index] = p[0]

			# remove o elemento
			del queue[-1]

			# organiza a fila
			queue = sorted(queue)
			if (count == len(goal)):
				return answer

		# verifica se ha nos nao visitados do no atual
		if (p[1] not in visited):
			for i in range(len(graph[p[1]])):
				# valor multiplicado por -1 para ir para o topo da fila
				queue.append( [(p[0] + cost[(p[1], graph[p[1]][i])])* -1, graph[p[1]][i]])

		# seta como visitado
		visited[p[1]] = 1

	return answer

# main
if __name__ == '__main__':
	
	# cria o grafo
	graph,cost = [[] for i in range(8)],{}

	graph[0].append(1)
	graph[0].append(3)
	graph[3].append(1)
	graph[3].append(6)
	graph[3].append(4)
	graph[1].append(6)
	graph[4].append(2)
	graph[4].append(5)
	graph[2].append(1)
	graph[5].append(2)
	graph[5].append(6)
	graph[6].append(4)

	cost[(0, 1)] = 2
	cost[(0, 3)] = 5
	cost[(1, 6)] = 1
	cost[(3, 1)] = 5
	cost[(3, 6)] = 6
	cost[(3, 4)] = 2
	cost[(2, 1)] = 4
	cost[(4, 2)] = 4
	cost[(4, 5)] = 3
	cost[(5, 2)] = 6
	cost[(5, 6)] = 3
	cost[(6, 4)] = 7

	goal = []
	goal.append(6)
	answer = uniform_cost_search(goal, 0)

	# Exibe a resposta
	print("O custo mínimo de 0 a 6 é =",answer[0])
