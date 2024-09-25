#ORDENAR LOS NUMEROS DE MENOR A MAYOR

numbers = [99, 14, 5]  # 3 elementos

# len(numbers) retorna la cantidad de elmenetos en la lista
quantity = len(numbers)  # 3

for i in range(quantity - 1):
    for j in range(quantity - 1 - i):
        value = numbers[j]
        if value > numbers[j+1]:
            numbers[j] = numbers[j+1]
            numbers[j+1] = value
            
print(numbers)