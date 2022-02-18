indice = float(input("Informe o índice de poluição: "))

if indice >= 0.3 and indice < 0.4:
    print("Atenção empresas do Primeiro grupo suspender as atividades! ")
elif indice >= 0.4 and indice < 0.5:
    print("Atenção empresas dos segundo grupo suspender as atividades. ")
elif indice >= 0.5:
    print("Todas as empresas devem suspender as atividades. ")


