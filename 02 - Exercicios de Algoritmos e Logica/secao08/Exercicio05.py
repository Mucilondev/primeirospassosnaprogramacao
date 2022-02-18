#Faça um programa que carregue um vetor com dez números inteiros.
#Calcule e mostre os números superiores a 50 e suas respectivas posições.
#Mostrar mensagem se não existir nenhum número nesta condição.

vetor = []
maiores_50 = False
for n in range(0, 10):
    num = int(input("Informe {0} valor para o vetor: ".format(n+1)))
    vetor.append(num)
for n in vetor:
    if n > 50:
        print("O Número {0} está na posição {1} do vetor".format(n, vetor.index(n)))
        maiores_50 = True
if maiores_50 == False:
    print("Não existe nenhum número maior que 50")