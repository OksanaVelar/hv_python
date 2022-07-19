# Задайте список из n чисел последовательности 1+(1/n)^n 
# и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
n = int(input('Введите любое число и нажмите "Enter": '))
lines = []
sum = 0
for i in range(1, n+1):
    result = (1+(1/i))**i
    lines.append(round(result, 2))
print (lines)
for i in lines:
    sum+= i

print (sum)
