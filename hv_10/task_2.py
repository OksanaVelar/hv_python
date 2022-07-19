# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# shed = [1, 5, 7, 12, 4, 9, 1]
# result = 0
# def mult(el):
#     el
#     for el in range (len(shed)):
#         if len(shed)//2:
#             return shed[]
   

# print(new_shed)

# shed = [1,5,7,12,4,9,1]

# def Multi(arr: list):
#     lastin = len(arr)-1
#     for i in range(len(arr)//2):
#         print(arr[i]*arr[lastin-i])


# print(Multi(shed))

shed = [1,5,7,12,4,9,1,4]

def Multi(arr: list):
    size = len(arr)-1
    arra = []
    for i in range(len(arr)//2):
        arra.append(arr[i]*arr[size-i])
    return arra

new_list = Multi(shed)
print(new_list)