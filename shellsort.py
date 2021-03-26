import random
import time

length = int(input('Digite o tamanho do vetor: '))
numbers = list(range(0, length))
random.shuffle(numbers)
print('Vetor original:')
print(numbers)


def shellSort(numbers):
    numberOfIterationsOrdination = 0
    h = len(numbers)//2
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
        numberOfIterationsOrdination += 1
        h = h // 2
    print('\nIterações Shellsort: {}'.format(numberOfIterationsOrdination))


def searchElement(element, array):
    numberOfIterationsSearch = 0
    for i in array:
        numberOfIterationsSearch += 1
        if i == element:
            print('O número {} se encontra na posição {}.'.format(
                element, array.index(i)))
            break
    print('Iterações de busca: {}'.format(numberOfIterationsSearch))


beforeOrdination = time.time()
shellSort(numbers)
afterOrdination = time.time()
totalOrdination = (afterOrdination - beforeOrdination)*1000
print('Vetor ordenado:')
print(numbers)
print('Tempo total para ordenação: %.2f ms' % totalOrdination)
print('')

element = int(input('Digite o número a ser buscado: '))
beforeSearch = time.time()
searchElement(element, numbers)
afterSearch = time.time()
totalSearch = (afterSearch - beforeSearch)*1000
print('Tempo total para busca: %.2f ms' % totalSearch)
print('')
