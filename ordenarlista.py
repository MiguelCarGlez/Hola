def ordenarLista(lista):
    if lista[0] <= lista[1] or (lista[1]-1) == lista[0]:
        if len(lista)==2:
            return True
        else:
            return ordenarLista(lista[1:])
        
    else:
        return False
    

lista = [4,4,4]
print(ordenarLista(lista))