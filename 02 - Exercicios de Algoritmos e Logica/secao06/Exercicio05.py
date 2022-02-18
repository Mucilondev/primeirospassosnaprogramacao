p = float(input("Informe o peso dos peixes: "))
if p > 50:
    m = (p - 50) * 4.00
    e = 'excesso'
else:
    m = 0
    e = 0
print("Multas: R${0}".format(m))
print("Excesso: {0}".format(e))
