# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N

n = int(input('Введите любое натуральное число и нажмите "Enter": '))

for i in range (n-1, 1, -1):
    prime = 0
    if(n % i == 0):
        for j in range(i-1, 1, -1):
            if(i % j == 0):
                prime += 1
        if(prime == 0):
            print (i)


