import random
import time

length = int(input('Digite o tamanho do vetor: '))

numbers = list(range(0, length))
random.shuffle(numbers)
print('Vetor original:')
print(numbers)


def shellSort(numbers):

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
        h = h // 2


def searchElement(element, array):
    for i in array:
        if i == element:
            print('O número {} se encontra na posição {}.'.format(
                element, array.index(i)))


before = time.time()
shellSort(numbers)
after = time.time()

total = (after - before)*1000
print('Vetor ordenado:')
print(numbers)
print('Tempo total: %.2f ms' % total)
print('')

element = int(input('Digite o número a ser buscado: '))
searchElement(element, numbers)
