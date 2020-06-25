#Escreva um programa que abra um arquivo digitado pelo usuário e imprima seu conteúdo na tela.  

"""
Nesse exemplo criamos um arquivo chamado "arquivo.fasta" na mesma pasta do script para testes com o conteudo abaixo.

>sp|Q9SE50|BGL18_ARATH Beta-D-glucopyranosyl abscisate beta-glucosidase OS=Arabidopsis thaliana OX=3702 GN=BGLU18 PE=1 SV=2
MVRFEKVHLVLGLALVLTLVGAPTKAQGPVCGAGLPDKFSRLNFPEGFIWGTATAAFQVE
GAVNEGCRGPSMWDTFTKKFPHRCENHNADVAVDFYHRYKEDIQLMKDLNTDAFRLSIAW
PRIFPHGRMSKGISKVGVQFYHDLIDELLKNNIIPLVTVFHWDTPQDLEDEYGGFLSGRI
VQDFTEYANFTFHEYGHKVKHWITFNEPWVFSRAGYDNGKKAPGRCSPYIPGYGQHCQDG
RSGYEAYQVSHNLLLSHAYAVDAFRNCKQCAGGKIGIAHSPAWFEPQDLEHVGGSIERVL
DFILGWHLAPTTYGDYPQSMKDRVGHRLPKFTEAEKKLLKGSTDYVGMNYYTSVFAKEIS
PDPKSPSWTTDSLVDWDSKSVDGYKIGSKPFNGKLDVYSKGLRYLLKYIKDNYGDPEVII
AENGYGEDLGEKHNDVNFGTQDHNRKYYIQRHLLSMHDAICKDKVNVTGYFVWSLMDNFE
WQDGYKARFGLYYIDFQNNLTRHQKVSGKWYSEFLKPQFPTSKLREEL


"""
nome_arquivo = input("Digite o nome do arquivo que você deseja abrir ") #Recebe o nome do arquivo

arquivo = open(nome_arquivo) #Abrir o arquivo

linhas = arquivo.readlines() #Ler as linhas do arquivo

for linha in linhas:
	print(linha.strip()) #.strip para remover os caracteres especiais
