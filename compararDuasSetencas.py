#Escreva um programa que compare se duas sequências digitadas pelo usuário são iguais.   
#Python 2 é preciso usar raw_input e não somente input

seq1 = input("Por favor, informe a primeira sequência para comparação: ")
seq2 = input("Por favor, informe a segunda sequência para comparação: ")

if seq1 == seq2:
	print("As sequências digitadas são iguais!")
else:
	print("As sequências digitadas são diferentes!")
	
#Outro método

import re

seq1 = input("Por favor, informe a primeira sequência para comparação: ")
seq2 = input("Por favor, informe a segunda sequência para comparação: ")


busca = re.match(seq1,seq2)

if busca:
	print("Sequências idênticas")
	print(busca.group())
else:
	print("Sequências Diferents")


