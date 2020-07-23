#!/usr/bin/env python
# -*- coding: utf-8 -*-

baixo = 0
lista = [1,2,3,4,5,6,7,8,9,10]
contador = 0

def binary_search(lista,item):
    baixo = 0
    alto = len(lista)-1
    global contador 
    
    while baixo <= alto:
        meio = (baixo + alto) / 2
        chute = lista[meio]
        
    
        if chute == item:
            return meio
        if chute > item:
            alto = meio -1
        
        else:
            baixo = meio + 1
        
        contador = contador + 1

    contador = 0    
    return None



result = binary_search(lista,-1)
print "resultado encontrado em {}: posição:{}".format(contador,result) 
    


