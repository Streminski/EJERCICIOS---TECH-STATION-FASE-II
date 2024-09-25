def ordenar(numbers):
    quantity = len(numbers)  # 3

    for i in range(quantity - 1):
        for j in range(quantity - 1 - i):
            value = numbers[j]
            if value > numbers[j+1]:
                numbers[j] = numbers[j+1]
                numbers[j+1] = value
                
    return numbers



cantidad_notas_pedidas = 3
cantidad_notas_ingresadas = 0
sumatoria_notas = 0

nota_mayor = 0

listado_de_notas = []

# hacer mientras (la condicion se cumpla)
while cantidad_notas_ingresadas < cantidad_notas_pedidas:
    nota = float(input("Ingresar nota del estudiante: "))
    
    listado_de_notas.append(nota)
    
    sumatoria_notas = sumatoria_notas + nota
    
    if nota > nota_mayor:
        nota_mayor = nota
    
    cantidad_notas_ingresadas += 1
    
promedio = sumatoria_notas / cantidad_notas_pedidas
promedio = round(promedio, 2)

print(f"Promedio: {promedio}")
print("Nota mayor: ", nota_mayor)
print("listado de notas: ", listado_de_notas)


lista_de_notas_ordenadas = ordenar(listado_de_notas)
print("listado de notas ordenadas: ", lista_de_notas_ordenadas)
