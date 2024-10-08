numero1 = int(input("Ingresar el 1er valor: "))
numero2 = int(input("Ingresar el 2do valor: "))

operacion = input("Seleccionar operación (1-sumar 2-restar 3-multiplicar 4-dividir): ")

operaciones = {
    "sumar": numero1 + numero2,
    "restar": numero1 - numero2,
    "multiplicar": numero1 * numero2,
    "dividir": numero1 / numero2,
}

print(operaciones[operacion])
