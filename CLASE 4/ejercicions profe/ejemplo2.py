numero_1 = 50
numero_2 = 20

division = numero_1 / numero_2
print(division)


resultado = numero_1 % numero_2
print(resultado)


listado = [50, 25, 12, 6, 75, 3, 4, 50, 25]
listado_pares = []
listado_impares = []

for elemento in listado:
    if elemento % 2 == 0:
        listado_pares.append(elemento)
    else:
        listado_impares.append(elemento)
        
        
print(listado_pares)
print(len(listado_pares))

print(listado_impares)
print(len(listado_impares))
    




