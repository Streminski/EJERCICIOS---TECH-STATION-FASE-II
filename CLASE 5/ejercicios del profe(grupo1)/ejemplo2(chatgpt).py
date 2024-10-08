# Ingresar los dos números
numero1 = float(input("Ingresar número 1: "))
numero2 = float(input("Ingresar número 2: "))

# Mostrar menú de operaciones
operaciones = {
    "1": "suma",
    "2": "resta",
    "3": "multiplicación",
    "4": "división"
}

# Mostrar opciones de operación al usuario
print("Seleccione una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

# Ingresar opción de operación
opcion = input("Elige una operación (1/2/3/4): ")

# Ejecutar la operación seleccionada
if opcion == "1":
    resultado = numero1 + numero2
    print(f"El resultado de la suma es: {resultado}")
elif opcion == "2":
    resultado = numero1 - numero2
    print(f"El resultado de la resta es: {resultado}")
elif opcion == "3":
    resultado = numero1 * numero2
    print(f"El resultado de la multiplicación es: {resultado}")
elif opcion == "4":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"El resultado de la división es: {resultado}")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Opción inválida, por favor elige una opción del 1 al 4.")
