# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# 1 ВАРИАНТ
# shed = [1,5,7,3,73,59,345]
# new_shed = []
# sum = 0
# for i in range (len(shed)):
#     if i % 2 !=0:
#         new_shed.append(shed[i])
#         print(shed.pop(i))

# print(new_shed)

# for i in range (len(new_shed)):
#     sum = sum + new_shed[i]
# print(sum)

# 2 ВАРИАНТ
shed = [1,5,7,3,73,59,345]
sum = 0
i = 0
while i < len(shed):
    if i%2 != 0:
        sum += shed[i]
    i+=1

print(sum)


# 3 ВАРИАНТ
# shed = [1,5,7,3,73,59,345]
# sum = 0
# for i in range (len(shed)//2+1):
#     print(shed.pop(i))
#     print(shed)
# for i in range (len(shed)):
#     sum += shed[i]

# print(sum)
