import json

arquivo = open("dados.json")
faturamento = json.load(arquivo) # Interpreta o .json como uma lista de dicionários, cada dicionário correspondendo a uma linha de dados

'''
Será necessário percorrer os dados duas vezes,
pois primeiro é necessário calcular a média e em
seguida verificar quantos dias têm faturamento
superior à mesma.
'''
maiorValor = 0
diaMaiorValor = 0
somaFaturamentos = 0
diasConsiderados = 0

for dia in faturamento:
	if dia["valor"] > 0: # Dias onde o faturamento é 0 são ignorados
		diasConsiderados += 1
		if dia["valor"] > maiorValor:
			maiorValor = dia["valor"]
			diaMaiorValor = dia["dia"]
		somaFaturamentos += dia["valor"]

media = somaFaturamentos/diasConsiderados
menorValor = maiorValor
diaMenorValor = diaMaiorValor
diasFaturamentoSuperior = 0

for dia in faturamento:
	'''
	Só é especificado que os dias sem faturamento devem
	ser ignorados no cálculo da média. Entretanto, sem
	ignorá-los no cálculo do menor valor, esse seria
	trivial, pois seria necessariamente 0. Então
	foi considerado que deve-se fazer o mesmo aqui.
	'''
	if dia["valor"] > 0:
		if dia["valor"] < menorValor:
			menorValor = dia["valor"]
			diaMenorValor = dia["dia"]
		if dia["valor"] > media:
			diasFaturamentoSuperior += 1

print("O menor valor de faturamento ocorrido foi", menorValor, "no dia", diaMenorValor)
print("O maior valor de faturamento ocorrido foi", maiorValor, "no dia", diaMaiorValor)
print("O número de dias em que o valor de faturamento foi superior à média mensal foi", diasFaturamentoSuperior)
