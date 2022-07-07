entrada = "The quick brown fox jumps over the lazy dog 123" # String para ser invertida
invertida = ""

for i in range(-1, -len(entrada)-1, -1):
	invertida += entrada[i]

print("A string inicial foi \'", entrada, "\'")
print("A string invertida é \'", invertida, "\'")
