#SACAR UN PROMEDIO DE NOTAS Y MOSTRAR LA NOTA MAYOR

cantidad_notas_pedidas = 3
cantidad_notas_ingresadas = 0
sumatoria_notas = 0

nota_mayor = 0

# hacer mientras (la condicion se cumpla)
while cantidad_notas_ingresadas < cantidad_notas_pedidas:
    nota = float(input("Ingresar nota del estudiante: "))
    sumatoria_notas = sumatoria_notas + nota
    
    if nota > nota_mayor:
        nota_mayor = nota
    
    cantidad_notas_ingresadas += 1
    
promedio = sumatoria_notas / cantidad_notas_pedidas
promedio = round(promedio, 2)

print(f"Promedio: {promedio}")
print("Nota mayor: ", nota_mayor)
    
