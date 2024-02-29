bancos=["BB","Caixa","Santander"]
print(bancos)
#resultado:["BB","Caixa","Santander"]
bancos[1]= " Itaú"
print(bancos)
#resultado:["BB","Itaú","Santander"]
bancos[-1]= "C6"
print(bancos)
#resultado:["BB","Itaú","C6"]
bancos= bancos + ["bradesco","nubank"]
print(bancos)
#resultado:["BB","Itaú","C6","bradesco","nubank"]