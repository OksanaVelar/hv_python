# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
# from gettext import find

num1 = (input('Введите любое вещественное число и нажмите "Enter": '))
num = int(num1.replace('.', ''))
sum = 0
while num > 0:
    sum += num % 10
    num = num // 10
    
print(sum)


