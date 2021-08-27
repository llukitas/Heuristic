

lista = [10,2,36,7,81,9,46,57,6,]

def intercambia(lista):
    if len(lista):
        x = sorted(enumerate(lista), key=lambda y: y[1])
        menor = x[0][0]
        mayor = x[-2][0]
        lista[menor],lista[mayor] = lista[mayor],lista[menor]
    return lista

print(intercambia(lista))