# Please write a function named longest(strings: list), which takes a list of strings as its argument. The function finds and returns the longest string in the list. You may assume there is always a single longest string in the list.

def longest(list):
    length = len(list[0])
    long_word = list[0]
    for word in list:
        if len(word) > length:
            long_word = word
            length = len(word)
        else:
            continue
    return long_word



def verifica_pares_impares(lista):
    pares = []
    impares = []

    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            continue  
            impares.append(numero)

    return pares, impares

# EXEMPLO
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares, impares = verifica_pares_impares(numeros)
# Pares 2,4,6,8,10
# Impares 1,3,5,7,9

