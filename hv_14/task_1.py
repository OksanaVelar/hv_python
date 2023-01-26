# LAMBDA:
# напишите программу, которая найдёт произведение пары чисел списка. 
# парой считаем первый и последний элемент.

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

# LIST COMPREHENSION:
# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

shed = [1,5,7,3,73,59,345]
sum = 0
shed2 = [shed.pop(i) for i in range (len(shed)//2+1)] # LIST COMPREHENSION
print(shed2)
for i in range (len(shed2)):
    if i !=0:
        sum += shed2[i]

print(sum)
