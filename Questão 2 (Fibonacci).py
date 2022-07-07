entrada = 39 # Número para ser testado

if entrada == 0 or entrada == 1: # Devido à maneira como a recursão foi implementada, 0 e 1 se tornam casos especiais
	fazParte = True
else:
	fazParte = False

	fAnterior = 0 #Pode ser considerado f(n-1)
	fAtual = 1 #Pode ser considerado f(n)

	while fAtual < entrada:
		# Calcula o próximo valor da sequência
		fNovo = fAnterior + fAtual
		fAnterior = fAtual
		fAtual = fNovo

		if fAtual == entrada:
			fazParte = True
			break

if fazParte:
	print("O número pertence à sequência de Fibonacci.")
else:
	print("O número não pertence à sequência de Fibonacci.")
