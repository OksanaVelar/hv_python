# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных
''' 
    Создание закодированной строки
'''
def Uncode_parts(stroka):
    i = 0
    count = 1
    new_stroka = ''   
    for i in range (len(stroka)-1):
        
        if stroka[i]==stroka[i+1]:
            count+=1

        elif stroka[i]!=stroka[i+1]:
            if count > 1:
                new_stroka += "%d%s," % (count,stroka[i])
                count = 1
            else:
                new_stroka += stroka[i]+ ','
            if i == (len(stroka)-2):
                new_stroka += stroka[i+1]
    return new_stroka

original = 'напрррррррррррррррррррра-во!'
print()
print(f'Исходная строка: \n {original}')
print()
uncoded = Uncode_parts(original)
print (f'Закодированная строка: \n {uncoded}')
print()

# вывод символа (последний элемент строки)
def Get_last(S):
    if len(S) > 1:
        a = S[-1]
    else:
        a = S
    return a

# вывод индекса (все, что до последнего элемента строки)
def Get_Indx(e):
    if len(e) > 1:
        a = e[:-1]
    else:
        a = 1
    return a

# создание строки заданной длины по значению индекса
def Get_str (num, smbl):
    longstr = ''
    for i in range (int(num)):
        longstr += smbl
    return longstr

# основной код
back_str = ''
s1 = uncoded.split(',') #разбиение строки по запятым

for i in range (len(s1)):
    sr = s1[i] # выделение среза <индекс+символ>
    el = Get_last(sr) # вывод элемента (последний символ строки)
    ind = Get_Indx(sr) # вывод индекса (все, что до последнего символа строки)
    lnst = Get_str(ind,el) # создание строки из заданной длины
    back_str +=lnst # сборка восстанавливаемой строки
    
print(f'Восстановленная строка: \n {back_str}')
print()



