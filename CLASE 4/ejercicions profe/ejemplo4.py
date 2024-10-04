a = 30
b = 25
c = "30"
d = None
e = 30


resultado = (d is not None) and (a == 30 and b < 30) or (e == 30 and c == "22")
#              F           and (  V     and   V   ) or (  V     and     F    )
#              F           and           V          or           F   
#                           F                       or          F
#                                                   F    

print(resultado)

