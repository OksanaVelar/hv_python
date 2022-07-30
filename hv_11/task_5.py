# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов

with open ('text.txt', 'r') as file:
    pol1 = file.read()
print(f'Полином 1: {pol1}')
file.close()

with open('text2.txt', 'r') as file2:
    pol2 = file2.read()
print(f'Полином 2: {pol2}')
file.close()

def Shedmake(shed):
    newshed = []
    for i in range (len(shed)):
        if shed[i] == '*':
            newshed.append(int(shed[i-1]))
        else:
            continue
    return(newshed)

Shed1 = Shedmake(pol1)
Shed2 = Shedmake(pol2)

def sum (a, b):
    Sumshed = []
    for i in range (len(a)):
        Sumshed.append(a[i]+b[i])
    return(Sumshed)

Shed3 = sum(Shed1, Shed2)

def MakeFile(sps):
    s = ''
    degree = int(pol1[4])
    for i in range (len(sps)):
        if i == len(sps)-1:
            s = s+f'{sps[i]}*x**{degree}'
        else:
            s = s+f'{sps[i]}*x**{degree}+'
        degree += 1
        
    with open ('text3.txt', 'w') as file:
        file.write(s)
MakeFile(Shed3)

with open ('text3.txt', 'r') as file:
    pol3 = file.read()
print(f'Сумма полиномов: {pol3}')
file.close()







