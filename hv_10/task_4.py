# Напишите программу, которая будет преобразовывать десятичное число в двоичное
# ВАРИАНТ 1
# x = int(input('Введите любое натуральное число и нажмите "Enter": '))
# binnum = bin(x)
# print(binnum)

# ВАРИАНТ 2
x = int(input('Введите любое натуральное число и нажмите "Enter": '))
y = ''
while x > 0:
    y = str(x%2)+y
    x = x // 2
print(y)


    

