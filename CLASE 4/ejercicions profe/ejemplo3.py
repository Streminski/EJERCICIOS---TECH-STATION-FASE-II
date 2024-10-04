"""
a == b
a != b
mayor o igual >=  a >= b
menor o igual <=
asignación =
comparación ==    
"""

a = 30
b = 25
c = "30"
d = None
e = 30

resultado = a == b # False
resultado = a >= b # False
resultado = a < b # True

resultado = a <= b # True
resultado = (a < b) or (a == b)  # True

resultado = not (a == d)  # True

print(resultado)

print(a == e) 
print(a is d)


