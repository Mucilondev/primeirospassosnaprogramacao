#Faça um programa que receba um código numérico inteiro e um vetor de cinco
#posições de números reais. Se o código for zero, termine o programa
#Se o código for 1, mostre o vetor na ordem direta. Se o código for 2,
#mostre o vetor na ordem inversa

vetor = []
codigo = int(input("Informe o código:  "))
if codigo != 0:
    for n in range(0, 5):
        num = float(input("Informe um valor real: "))
        vetor.append(num)
    if codigo == 1:
        for n in vetor:
            print(n)
    if codigo == 2:
        vetor.reverse()
        for n in vetor:
            print(n)
