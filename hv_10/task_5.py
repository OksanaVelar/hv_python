# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов

# Очевидно, в условии задачи допущена неточность и вместо "отрицательных индексов"
# нужно рассматривать отрицательные числа...
# Привожу решение задачи, исходя из данной поправки

n = int(input('Введите любое целое число и нажмите "Enter": '))
def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

shed =[]
for i in range(-1, n+(-1)):
    shed.append(fib(i))
print(shed)

# n = int(input('Введите любое целое число и нажмите "Enter": '))
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# shed =[]
# for i in range(1,n):
#     shed.append(fib(i))
# print(shed)
