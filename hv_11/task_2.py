# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N
n = int(input('Введите любое натуральное число и нажмите "Enter": '))
shed = []
for i in range (n-1, 1, -1):
    prime = 0
    if(n % i == 0):
        for j in range(i-1, 1, -1):
            if(i % j == 0):
                prime += 1
        if(prime == 0):
            shed.append(i)
def Print_list(my_list):
    for i in range (len(my_list)):
        if i == len(my_list) -1:
            print (f'{my_list[i]}.')
        else:
            print(f'{my_list[i]},', end = '')

print(f'Простые множители числа {n}:', end = ' ')
Print_list(shed)




# n = int(input('Введите любое натуральное число и нажмите "Enter": '))
# shed = []
# for i in range (n-1, 1, -1):
#     prime = 0
#     if(n % i == 0):
#         for j in range(i-1, 1, -1):
#             if(i % j == 0):
#                 prime += 1
#         if(prime == 0):
#             shed.append(i)
# print(f'Простые множители числа {n} : {shed}')
#             # print (i, end = ', ')


