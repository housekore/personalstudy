#Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.   

nota1 = input("Digite a nota da primeira avaliação primeiro ")
nota2 = input("Digite a nota da segunda avaliação ")

media = (float(nota1) + float(nota2))/2
if media >= 6:
	print("Parabéns! Você foi aprovado com a média", media)

else:
	print("Você foi reporvado, pois sua média foi", media)
