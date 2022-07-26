# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов

n1 = str(((5*2)**2) + ((3*3)**3))
n2 = str(2*5 - 6*2)
shed1 = []
shed2 = []
with open ('text.txt', 'w') as file:
    for i in n1:
        file.write(n1)
with open('text2.txt', 'w') as file2:
    for i in n2:
        file2.write(n2)




