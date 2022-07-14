# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
num = int(input('Введите любое число и нажмите "Enter": '))
list = []
result = 1
for i in range (1, num+1):
    result *= i
    list.append(result)
print (list)

