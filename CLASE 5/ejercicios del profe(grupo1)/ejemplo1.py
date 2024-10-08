nota = 0

# Si lo quiero trabajar con INPUT
# nota = float(input("Ingresar nota: "))

if nota >= 90 and nota <100:
    print("Obtiviste A")
elif nota >=80 and nota <90:
    print("Obtuviste B")
elif nota >= 70 and nota <80:
    print("Obtuviste C")
elif nota >=60 and nota <60:
    print("Obtuviste D")
elif nota <60:
    print("Reprobaste")
elif nota >100 or nota <0:
    print("Calificacion invalida")


