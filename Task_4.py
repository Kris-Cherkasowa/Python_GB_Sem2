#Задайте числами список из N элементов, заполненных из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
from random import randint
with open('file.txt', 'w') as data:
    data.write('2\n')
    data.write('5\n')
    data.write('8\n')
def list(N):
    return [randint(-N/2, N) for i in range(-N, N + 1)]
def get_position(path):
    data = open(path, 'r')
    pos = [int(line.strip()) for line in data]
    data.close()
    return pos
def result(numbers, position):
    res = 1
    for i in position:
        res *= numbers[i]
    return res
path = 'file.txt'
N = 10
numbers = list(N)
position = get_position(path)
get_result = result(numbers, position)
print(numbers)
print(position)
print(get_result)