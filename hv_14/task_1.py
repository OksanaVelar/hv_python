# Условие исходной задачи:
# напишите программу, которая найдёт произведение пары чисел списка. 
# парой считаем первый и последний элемент.

def calc(x, y):
    return x*y
f = calc
f = lambda x, y: x*y 

def calc2(a, b, op):
    return op(a, b)
f2 = calc2

shed = [1,5,7,12,4,9,1,4]
size = len(shed)-1
i = 0
part1 = shed[i]
part2 = shed[size-i]
rez = f2(part1, part2, lambda part1, part2: part2*part1)

print (rez)


