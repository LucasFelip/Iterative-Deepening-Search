# Retorna o menor caminho
def ucs(vertDes, vertIni):
	
	global grafo, custo
	custos = []

	# Cria uma fila de prioridades
	filaPrio = []

	# Diz que todos os caminhos sao infinitos
	for i in range(len(vertDes)):
		custos.append(10**8)

	# poe na fila o primeiro vertice
	filaPrio.append([0, vertIni])

	# guarda os nós visitados
	visitados = {}
	contador = 0

	# Enquanto a fila nao estiver vazia
	while (len(filaPrio) > 0):

		# Pega o elemento no topo da fila
		filaPrio = sorted(filaPrio)
		maiorEle = filaPrio[-1]

		# remove o elemento
		del filaPrio[-1]

		# pega o valor original
		maiorEle[0] *= -1

		# verifica se o elemento faz parte do objetivo
		if (maiorEle[1] in vertDes):

			# pega a posicao
			index = vertDes.index(maiorEle[1])

			# se um novo caminho for encontrado
			# aumenta o contador
			if (custos[index] == 10**8):
				contador += 1

			# se o custo eh menor, garda o custo
			if (custos[index] > maiorEle[0]):
				custos[index] = maiorEle[0]

			# remove o elemento
			del filaPrio[-1]

			# organiza a fila
			filaPrio = sorted(filaPrio)
			if (contador == len(vertDes)):
				return custos

		# verifica se ha nos nao visitados do no atual
		if (maiorEle[1] not in visitados):
			for i in range(len(grafo[maiorEle[1]])):

				# valor multiplicado por -1 para ir para o topo da fila
				filaPrio.append( [(maiorEle[0] + custo[(maiorEle[1], grafo[maiorEle[1]][i])])* -1, grafo[maiorEle[1]][i]])

		# seta como visitado
		visitados[maiorEle[1]] = 1

	return custos

# cria o grafo
grafo,custo = [[] for i in range(8)],{}

grafo[0].append(1)
grafo[0].append(3)
grafo[3].append(1)
grafo[3].append(6)
grafo[3].append(4)
grafo[1].append(6)
grafo[4].append(2)
grafo[4].append(5)
grafo[2].append(1)
grafo[5].append(2)
grafo[5].append(6)
grafo[6].append(4)

custo[(0, 1)] = 2
custo[(0, 3)] = 5
custo[(1, 6)] = 1
custo[(3, 1)] = 5
custo[(3, 6)] = 6
custo[(3, 4)] = 2
custo[(2, 1)] = 4
custo[(4, 2)] = 4
custo[(4, 5)] = 3
custo[(5, 2)] = 6
custo[(5, 6)] = 3
custo[(6, 4)] = 7

goal = []
goal.append(6)
answer = ucs(goal, 0)

# Exibe a resposta
print("Custo minimo de 0 ate 6 eh = ",answer[0])