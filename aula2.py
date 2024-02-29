soma= 0 
contar= 0 
for i in range (1,8):
    num = int (input(f'Digite o {i}º número:'))

    if num % 2 == 0:
        soma += num
        contar+= 1

print(f'A soma dos {contar}numeros pares foi igual a {soma}')
