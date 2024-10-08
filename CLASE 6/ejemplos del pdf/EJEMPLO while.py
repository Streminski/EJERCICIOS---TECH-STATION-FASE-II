i = 1
while i <= 10:
    print(i)
    i = i + 1 # o puede ser i += 1

suma = 0
i = 1
while i <= 5:
    suma += i
    i += 1
print("La suma es:", suma)

numero = int(input("Ingrese un número: "))
while numero >= 0:
    print("El número ingresado es:", numero)
    numero = int(input("Ingrese otro número: "))
print("Se ingresó un número negativo. Fin del ciclo.")