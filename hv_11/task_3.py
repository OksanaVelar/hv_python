# Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности

orshed = [1,8,3,9,5,6,0,9,4,4,4,1]
print(f'Исходная последовательность: {orshed}')
reshed =[]
for i in orshed:
    if i not in reshed:
        reshed.append(i)

# print(reshed)
print(f'Измененная последовательность: {reshed}')
