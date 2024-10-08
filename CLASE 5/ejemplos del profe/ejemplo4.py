valor = int(input("Ingresar valor: "))

if valor > 100 or valor < 0:
    print("Calificación inválida")
elif valor >= 90:
    print("Obtuviste una A")
elif valor >= 80 and valor < 90:
    print("Obtuviste una B")
elif valor >= 70 and valor < 80:
    print("Obtuviste una C")
elif valor >= 60 and valor < 70:
    print("Obtuviste una D")
else:
    print("Reprobaste")
