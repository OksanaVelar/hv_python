# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt 
# в одной строке одно число.
import random

n = int(input('Введите любое число и нажмите "Enter": '))
file = open('text.txt', 'w')
ind = random.randint(0,n) 
file.write(str(ind)+'\n')
file.write(str(random.randint(0,n)))
string = []
for i in range (n):
    string.append(random.randint (-n, n))
result = 1
with open('text.txt', 'r') as f:
    result *= string[int(f.read())]
print (string)
print(result)

file.close()