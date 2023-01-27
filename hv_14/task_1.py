"""
LAMBDA:
напишите программу, которая найдёт произведение пары чисел списка. 
парой считаем первый и последний элемент.
"""
# def calc(x, y):
#     return x*y
# f = calc
# f = lambda x, y: x*y 

# def calc2(a, b, op):
#     return op(a, b)
# f2 = calc2

# shed = [1,5,7,12,4,9,1,4]
# size = len(shed)-1
# i = 0
# part1 = shed[i]
# part2 = shed[size-i]
# rez = f2(part1, part2, lambda part1, part2: part2*part1)

# print (rez)
"""
LIST COMPREHENTION:
Задайте список из нескольких чисел. Напишите программу, 
которая найдёт сумму элементов списка, стоящих на нечётной позиции.
"""
# shed = [1,5,7,3,73,59,345]
# sum = 0
# shed2 = [shed.pop(i) for i in range (len(shed)//2+1)] # LIST COMPREHENSION
# print(shed2)
# for i in range (len(shed2)):
#     if i !=0:
#         sum += shed2[i]

# print(sum)
"""""
LAMBDA и LIST COMPREHENTION :
Задайте список из вещественных чисел. Напишите программу, 
которая найдёт разницу между максимальным и минимальным значениями 
дробной части элементов.
"""

# shed = [1.1, 5.2, 7.9, 12.6]
# print(f'Массив вещественных чисел : {shed}')
# new_shed = [int(shed[i]*10)%10 for i in range (len(shed))] # LIST COMPREHENSION
# print(f'Массив дробных частей элементов вышеприведенного массива : {new_shed}')

# def Math(x,y):
#     return x-y

# for i in range(1,len(new_shed)):
#     num = new_shed[i]
#     if i == 1:
#         max = num
#     elif max < num:
#         max = num
# print(f'Максимальное значение дробной части = {max}')

# min = new_shed[0]
# size = len(new_shed)
# i = 0
# while (i < size):
#     if(min > new_shed[i]):
#         min = new_shed[i]
#     i+=1

# print(f'Минимальное значение дробной части = {min}')
# def calc(op, a,b):
#     return op(a,b)

# w = calc(lambda x, y: x - y, max, min) # LAMBDA
# print(f'Разность максимального и минимального значений = {w}')

"""
LIST COMPREHENTION, LAMBDA, MAP
Напишите программу, которая принимает на вход координаты двух точек 
и находит расстояние между ними в 2D пространстве
"""

coord_A = []
coord_B = []
arr_points = []
i = 0
q = None
q1 = None

while i <= 3:
    if i <= 1:
        print('Введите значение координату "x" точки A и нажмите "Enter": ')
        q = int(input())
        coord_A.append(q)
        i = i+1
    else:
        print('Введите значение координаты точки В и нажмите "Enter": ')
        q1 = int(input())
        coord_B.append(q1)
        i = i+1
print(f'Координаты точки A: {coord_A} \nКоординаты точки B: {coord_B}')

def mathem (arr):
    e = arr[0]-arr[1]
    return e

a = mathem(coord_A)
b = mathem(coord_B)
arr_points.append(a)
arr_points.append(b)
print (arr_points)

def math2 (l):
    return l**2

square_A = list(map(math2, arr_points))
print (square_A)

import math
def Sum (op, s,c):
    t = op(s,c)
    return t

sum = Sum(lambda s,c: s+c, square_A[0], square_A[1])
sqrt = math.sqrt(sum)
print (f'Расстояние между заданными точками = {sqrt}')