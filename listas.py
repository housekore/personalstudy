#Criando as listas
minha_lista1 = ["abacaxi", "melância", "abacate", "uva", "morango"]
minha_lista2 = [1,2,3,4,5,6,7,8,9,10]
minha_lista3 = ["José Jardel", "Greice Kely", 95, 123, "Sofia", "Emily", "Gabriel"]

#Imprimir cada lista
print(minha_lista1)
print(minha_lista2)
print(minha_lista3)
print(minha_lista1[2]) #imprimir por indices

#imprimir por laço de repetição
for item in minha_lista1: 
	print(item)

#Verificar o tamanho da lista
tamanho = len(minha_lista1) 
print(tamanho)

#Adicionando Limão a lista 1
minha_lista1.append("Limão") 
print(minha_lista1)

#verificar se o item 7 está na lista
if 7 in minha_lista2: 
	print("7 Está na minha lista")
else:
	print("7 não está na minha lista")

#Deletar um item de uma lista
del minha_lista3[2:] #Deletar todos os itens a partir do item 2 até o final
print(minha_lista3)

del minha_lista3[:] #Deleta todos os itens
print(minha_lista3)
