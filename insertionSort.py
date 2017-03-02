# ALGORITMO INSERTION SORT - CÓDIGO

# ==== VETOR PARA SER ORDENADO
Elementos = [0,5,3,5,4,6,0,-1,15,50,3,4,50,80,9,10,11,8,7,6,5,4,3,2,1]

# === MOSTRA ESTADO INICIAL DO VETOR ===
print("Antes do algoritmo Insertion Sort: ")
print(Elementos, "\n")

# ALGORITMO INSERTION SORT
ChaveAtual = 0
for j in range(1, len(Elementos)):
	ChaveAtual = Elementos[j]
	i = j - 1

	while (i >= 0 and Elementos[i] > ChaveAtual):
		Elementos[i+1] = Elementos[i]
		i = i - 1
	Elementos[i+1] = ChaveAtual

# === MOSTRA O RESULTADO DEPOIS DA ORDENAÇÃO
print("Depois do algoritmo Insertion Sort: ")
print(Elementos)
