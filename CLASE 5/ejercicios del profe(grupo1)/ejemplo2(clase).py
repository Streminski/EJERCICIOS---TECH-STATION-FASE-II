# Pedimos al usuario que ingrese el primer número y lo convertimos a float para aceptar decimales
num1 = float(input("Ingresar número 1: "))

# Pedimos al usuario que ingrese el segundo número, también convertido a float
num2 = float(input("Ingresar número 2: "))

# Solicitamos al usuario que seleccione una operación entre las opciones listadas
operacion = input("1 - Suma\n2 - Resta\n3 - Multiplicacion\n4 - Division\nIngresar la operación que desea realizar:\n")

# Diccionario que actúa como un 'switch-case'. Las claves son los números de las operaciones (como strings).
# Los valores son cadenas formateadas (f-strings) que incluyen el resultado de la operación correspondiente.
opcion = {
    "1": f"Suma: {num1 + num2}",                # Si elige "1", realiza la suma de num1 y num2.
    "2": f"Resta: {num1 - num2}",               # Si elige "2", realiza la resta de num1 y num2.
    "3": f"Multiplicacion: {num1 * num2}",      # Si elige "3", realiza la multiplicación de num1 y num2.
    "4": f"Division: {num1 / num2}"             # Si elige "4", realiza la división de num1 entre num2.
}

# Usamos el diccionario para imprimir el valor asociado a la operación que el usuario eligió.
# Por ejemplo, si eligió "1", imprimirá el resultado de la suma.
print(opcion[operacion])
