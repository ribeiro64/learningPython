import random
import time

length = int(input('Digite o tamanho do vetor: '))
numberOfInteractions = 0
numbers = list(range(0, length))
random.shuffle(numbers)
print('Vetor original:')
print(numbers)


def shellSort(numbers):
    h = len(numbers)//2
    numberOfInteractions = 0
    while h > 0:
        i = h

        while i < len(numbers):
            temporary = numbers[i]
            changed = False
            j = i - h

            while j >= 0 and numbers[j] > temporary:
                numbers[j+h] = numbers[j]
                changed = True
                j -= h

            if changed:
                numbers[j+h] = temporary
            i += 1
        numberOfInteractions += 1
        h = h // 2
    return numberOfInteractions


def searchElement(element, array):
    for i in array:
        if i == element:
            print('O número {} se encontra na posição {}.'.format(
                element, array.index(i)))


beforeOrdination = time.time()
shellSort(numbers)
afterOrdination = time.time()
totalOrdination = (afterOrdination - beforeOrdination)*1000
print('Vetor ordenado:')
print(numbers)
print('Tempo total para ordenação: %.2f ms' % totalOrdination)
print('')

element = int(input('Digite o número a ser buscado: '))
beforeSerach = time.time()
searchElement(element, numbers)
afterSearch = time.time()
totalSerach = (afterSearch - beforeSerach)*1000
print('Tempo total para busca: %.2f ms' % totalSerach)
print('')
