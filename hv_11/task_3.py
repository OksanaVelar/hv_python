# Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности
# n = int(input('Введите максимальное число последовательности и нажмите "Enter": '))
# orshed = [1,8,3,9,5,6,0,9,4,4,4,1]
# print(orshed)
# dup = None
# checknum = None
# next = None

# for i in range(len(orshed)):
#     checknum = orshed[i]
#     for j in range(len(orshed)-1):
#         next = orshed[j+1]
#         if checknum == next:
#             dup == next
#             orshed.pop(dup)
        
orshed = [1,8,3,9,5,6,0,9,4,4,4,1]
print(f'Исходная последовательность: {orshed}')
reshed =[]
for i in orshed:
    if i not in reshed:
        reshed.append(i)

# print(reshed)
print(f'Измененная последовательность: {reshed}')


# def Print_list(shed):
#     for i in range (len(shed)):
#         if i == len(shed)-1:
#             print(f'{shed[i]}.')
#         else:
#             print(f'{shed[i]},', end = '')

# Print_list(result)


