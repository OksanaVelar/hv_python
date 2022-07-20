# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
shed = [1.1, 5.2, 7.9, 12.6]
print(f'Массив вещественных чисел : {shed}')
new_shed = []

for i in range (len(shed)):
    a = int((shed[i]*10)%10)
    new_shed.append(a)

print(f'Массив дробных частей элементов вышеприведенного массива : {new_shed}')

for i in range(1,len(new_shed)):
    num = new_shed[i]
    if i == 1:
        max = num
    elif max < num:
        max = num
print(f'Максимальное значение дробной части = {max}')

min = new_shed[0]
size = len(new_shed)
i = 0
while (i < size):
    if(min > new_shed[i]):
        min = new_shed[i]
    i+=1

print(f'Минимальное значение дробной части = {min}')
print(f'Разность максимального и минимального значений = {max-min}')

# for i in range(1, len(new_shed)):
#     num = new_shed[i]
#     if i == 1:
#         min = num
#     elif min > num:
#         min = num