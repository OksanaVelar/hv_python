# Условие сходной задачи:
# напишите программу, которая найдёт произведение пар чисел списка. 
# парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Решение исходной задачи:
# shed = [1,5,7,12,4,9,1,4]

# def Multi(arr: list):
#     size = len(arr)-1
#     arra = []
#     for i in range(len(arr)//2):
#        arra.append(arr[i]*arr[size-i])
#     return arra

# new_list = Multi(shed)
# print(new_list)

# решение задачи с лямбдой:
from re import X


shed = [1,5,7,12,4,9,1,4]
# def oprc(x,y):
#     return x*y
oprc = lambda x,y: x*y

def Multi(arr: list):
    size = len(arr)-1
    arra = []
    x = arr[i]
    y = arr[size-1]
    w = oprc
    for i in range(len(arr)//2):
        arra.append(w)
    return arra

new_list = Multi(shed)
print(new_list)

