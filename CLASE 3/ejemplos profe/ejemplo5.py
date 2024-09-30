numero1 = 200
numero2 = 300
numero3 = 400

resultado = (numero1 <= numero2) or (numero1 > numero3)
#                    f                        f
#                                 f

resultado = not (numero1 < numero2)
#                        V
#           F

print(resultado)
