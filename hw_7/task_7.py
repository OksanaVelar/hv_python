# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt
# в одной строке одно число.
import random

n = int(input('Введите любое число и нажмите "Enter": '))
file = open('text.txt', 'w')
file.write(str(random.randint(0, n-1)) + '\n')
file.write(str(random.randint(0, n-1)))
file.close()

lines = []
for i in range(n):
    lines.append(random.randint(-n, n))
print (lines)

file = open('text.txt', 'r')
inds = list()
for line in file:
    inds.append(int(line))
result=1
for i in inds:
    result*= lines[i]
print (result)
file.close()
