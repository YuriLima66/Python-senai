#convertendo uma lista em tuplas
lista_carros = ["gol","corolla", "ranger", "kadett","fusca", "clio"]
tupla_carros=tuple(lista_carros)
print(f"Tupla carros:{tupla_carros}")

#convertendo uma tupla em lista
tupla_carros = "gol","corolla", "ranger", "kadett","fusca", "clio"
lista_carros = list(tupla_carros)
print(f"Lista carros:{lista_carros}")

#desempacotando elementos da tupla
tupla_carros = "golf","corolla", "civic"
carro1, carro2, carro3 = tupla_carros
print(f"Carro1: {carro1}")
print(f"Carro2: {carro2}")
print(f"Carro3: {carro3}")

#desempacotando elementos da tupla usando atribuição multipla
tupla_carros = "golf","corolla", "civic", "opala","tucson","elantra"
carro2, *carros = tupla_carros
print(f"Carro1: {carro2}")
print(f"Carros: {carros}") #lista com os itens restantes