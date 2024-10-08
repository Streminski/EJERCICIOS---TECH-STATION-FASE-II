numero1 = int(input("Ingresar el 1er valor: "))
numero2 = int(input("Ingresar el 2do valor: "))

operacion = input("Seleccionar operación (1-sumar 2-restar 3-multiplicar 4-dividir): ")

match (operacion):
    case "1":
        print(numero1 + numero2)
    case "2":
        print(numero1 - numero2)
    case "3":
        print(numero1 * numero2)
    case "4":
        print(numero1 / numero2)
