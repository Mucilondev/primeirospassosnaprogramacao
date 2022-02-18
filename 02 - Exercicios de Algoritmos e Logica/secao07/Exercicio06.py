#Desenvolva um gerador de tabuada, capax de gerar a tabuada de qualquer numero inteiro#
#entre 1 a 10. O Usuário deve informar de qual número ele deseja ver a tabuada.#
numero = int(input("Informe um número: "))
while numero < 1 or numero > 10:
    numero = int(input("Informe um número 1 e 10"))
print("Tabuada de {0}".format(numero))
for n in range(1, 11):
    print("{0} x {1} = {2}".format(numero, n, (numero * n)))