#sua organizacao acaba de contratar um estagiario para trabalhar no suprote de informatica
#com a intencao de fazer um levantamento nas sucatas encontradas nesta área. A primeira
#tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando
#o estado de cada um deles, para verificar o que se pode aproveitar deles . Foi requisitado
#que você desenvolva um programa para registrar este levantamento. O programa deverá receber
#um número indeterminado de entradas, cada um contendo: um numero de identificação do mouse
#o tipo de defeito:
#- Necessita esfera:
#- Necessita de limpeza:
#- Necessita troca de cabo ou conector
#- Quebrado ou Inutilizado
#Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o
#seguinte relatório:

#Quantidade de mouses 100

#Situação                                      Quantidade             Percentual
#- Necessita esfera:                              40                      40%
#- Necessita de limpeza:                          30                      30%
#- Necessita troca de cabo ou conector            15                      15%
#- Quebrado ou Inutilizado                        15                      15%

##Variaveis
contador_total = 0
contador_sit_1 = 0
contador_sit_2 = 0
contador_sit_3 = 0
contador_sit_4 = 0
#Entrada
indentificador = int(input("Informe a Identificação: "))
#Entrada / Processamento
while indentificador !=0:
    print("1 - Necessidade de esfera: ")
    print("2 - Necessidade de limpeza: ")
    print("3 - Necessidade de troca do cabo ou conector: ")
    print("4 - Quebrado ou Inutilizavel: ")
    #Entrada
    defeito = int(input("Informe o tipo de defeito: "))
    #Processamento
    if defeito == 1:
        contador_sit_1 = contador_sit_1 + 1
    elif defeito == 2:
        contador_sit_2 = contador_sit_2 + 1
    elif defeito == 3:
        contador_sit_3 = contador_sit_3 + 1
    elif defeito == 4:
        contador_sit_4 = contador_sit_4 + 1
    contador_total = contador_total + 1
    indentificador = int(input("Informe a Identificação: "))
p1 = contador_sit_1 / contador_total * 100.0
p2 = contador_sit_2 / contador_total * 100.0
p3 = contador_sit_3 / contador_total * 100.0
p4 = contador_sit_4 / contador_total * 100.0
print("Quantidade total de Mouses: {0}".format(contador_total))
print("        Situação                               Quantidade        Porcentual")
print("1 - Necessidade de esfera                          {0}              {1:.2f}%".format(contador_sit_1, p1))
print("2 - Necessidade de limpeza                         {0}              {1:.2f}%".format(contador_sit_2, p3))
print("3 - Necessidade de troca do cabo ou conector       {0}              {1:.2f}%".format(contador_sit_3, p3))
print("4 - Quebrado ou Inutilizado                        {0}              {1:.2f}%".format(contador_sit_4, p4))
