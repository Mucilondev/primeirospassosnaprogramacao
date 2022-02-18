#Faça um algoritmo que carregue um vetor de 5 elementos inteiros e em seguida armazene
#em um vetor apenas os números pares maiores que 0. No final deve mostrar os elementos
#do vetor na tela.
vetor = []
pares = []
#OBS: estrutura lista vazia - acima ^^

for n in range(1, 6):
    vetor.append(n)  #apend = adiciona ao final do vetor o "n" que é passado dentro dos parenteses
    if n% 2 == 0:  #se o módulo, ou resto da divisao de n % 2 significa que ele é par
        pares.append(n)
for p in pares:
    print(p)



