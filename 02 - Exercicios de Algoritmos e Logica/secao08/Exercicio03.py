#Faça um programa que carregue um vetor com dez números inteiros. Mostre o vetor na ordem inversa a
#que foi digitado.

vetor = []
for n in range(0, 10):
    num = int(input("Informe o valor para o vetor: "))
    vetor.append(num)
#Processamento
vetor.reverse() #inverte a lista
for n in vetor:
    print(n)