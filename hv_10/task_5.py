# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов

n = int(input('Введите любое целое число и нажмите "Enter": '))
def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

shed =[0, 1]
for i in range(2, n+1):
    shed.append(fib(i))
print(shed)
nega_shed =[]
for i in range(len(shed)-1, 0, -1):
    if (i%2==0):
        nega_shed.append(shed[i]*(-1))
    else:
        nega_shed.append(shed[i])

print(nega_shed + shed)
