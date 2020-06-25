#Criamos o dicionário, separando cada indice por ,
meu_dicionario = {"A": "ALANINA", "B": "BCAA", "C": "CREATINA", "D": "WHEY", "E": "GLUTAMINA"}

#Chamando a chave, no exemplo a A
#Lembrando ser case sensitive
print(meu_dicionario["A"])

#Imprimir todo o dicionario
print(meu_dicionario)

#Usando FOR
for chave in meu_dicionario:
	print(meu_dicionario[chave])

#Usando FOR e concatadenando
for chave in meu_dicionario:
	print(chave+"-"+meu_dicionario[chave])

#Usando tupla - Conjunto de dados imutáveis
for i in meu_dicionario.items():
	print(i)

#Retornando apenas os valores de cada célula
for i in meu_dicionario.values():
	print(i)
