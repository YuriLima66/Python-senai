compras = ["arroz" , "bacon" , "cerveja", "oleo","alho","frango","ovo","sabão","manteiga","leite"]
print(f"tamanho da lista: {len(compras)}")

qtdtentativas = 1
while qtdtentativas<= len(compras):    
    
    var=str(input('informe um item '))
    if var.lower() in compras:
        print(f"o item'{var.lower()}' esta na lista")
    else:
        print(f"O item'{var.lower()}'não esta na lista")
    qtdtentativas= qtdtentativas+1

       