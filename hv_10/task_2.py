# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# 
# 1 ВАРИАНТ
# shed = [1,5,7,12,4,9,1]

# def Multi(arr: list):
#     lastin = len(arr)-1
#     for i in range(len(arr)//2):
#         print(arr[i]*arr[lastin-i])


# print(Multi(shed))

# 2 ВАРИАНТ
shed = [1,5,7,12,4,9,1,4]

def Multi(arr: list):
    size = len(arr)-1
    arra = []
    for i in range(len(arr)//2):
        arra.append(arr[i]*arr[size-i])
    return arra

new_list = Multi(shed)
print(new_list)