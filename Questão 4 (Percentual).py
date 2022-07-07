faturamento = {"SP" : 67836.43,
	"RJ" : 36678.66,
	"MG" : 29229.88,
	"ES" : 27165.48,
	"os demais estados" : 19849.53}

total = 0
for estado in faturamento:
	total += faturamento[estado]

for estado in faturamento:
	print("Para", estado, "o percentual de representação é de", (faturamento[estado]/total)*100, "%")
