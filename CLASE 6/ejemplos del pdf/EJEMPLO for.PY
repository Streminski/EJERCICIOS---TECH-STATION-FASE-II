for i in range(1, 11):
    print (i)

suma = 0
for i in range(1, 6):
    suma = suma + i  # o puede ser suma += i
print("la suma es: ", suma)

n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("El factorial de", n, "es:", factorial)