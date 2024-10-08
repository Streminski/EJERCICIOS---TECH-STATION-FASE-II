i = 1
while True:
    print(i)
    i = i + 1
    if i > 10:
        break

suma = 0
i = 1
while True:
    suma = suma + i
    i = i + 1
    if i > 5:
        break
print("la suma es: ", suma)


while True:  # Ciclo infinito hasta que se rompa con 'break'
    numero = int(input("Ingrese un número: "))  # Se pide un número al usuario
    if numero >= 0:
        print("El número ingresado es:", numero)  # Si el número es positivo o cero, se imprime
    else:
        print("Se ingresó un número negativo. Fin del ciclo.")  # Mensaje cuando se ingresa un número negativo
        break  # Rompe el ciclo cuando se ingresa un número negativo
