def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0

    for i in range(1,(len(arr))):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i

    return menor_indice

def ordenacao_por_selecao(arr):
    novo_arr = []

    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novo_arr.append(arr.pop(menor))

    return novo_arr

array_ordenado_por_selecao = ordenacao_por_selecao([5,3,2,8,1])

print array_ordenado_por_selecao