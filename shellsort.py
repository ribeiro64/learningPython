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


before = time.time()
shellSort(numbers)
after = time.time()

total = (after - before)*1000
print('Vetor ordenado:')
print(numbers)
print('Tempo total: %.2f ms' % total)
