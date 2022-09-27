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
        
        else: 
            new_stroka += "%d%s," % (count,stroka[i])
            count = 1

        if i == (len(stroka)-2):
            new_stroka += "%d%s" % (count,stroka[i+1])
    
    return new_stroka

# original = 'ФФОТТ'
# original = 'иллюминатор'
original = 'напрррррррррррррррррррра-во!'
print()
print(f'Исходная строка: \n {original}')
uncoded = Uncode_parts(original)
print (f'Закодированная строка: \n {uncoded}')

# разбиение строки по запятым
def Get_Temp_Str(ST):
    STR = ST.split(',')
    return STR

# выделение среза <индекс+символ>
def Splt (t):
    tt = t[i]
    return tt

# вывод элемента (последний символ строки)
def Get_last(S):
    return S[-1]

# вывод индекса (все, что до последнего символа строки)
def Get_Indx(e):
    return e[:-1]

# создание строки из заданной длины
def Get_str (num, smbl):
    longstr = ''
    for i in range (int(num)):
        longstr += smbl
    return longstr


back_str = ''
s1 = Get_Temp_Str(uncoded) #разбиение строки по запятым
# print(s1)

for i in range (len(s1)):
    sr = Splt (s1) # выделение среза <индекс+символ>
    # print(sr) 
    el = Get_last(sr) # вывод элемента (последний символ строки)
    # print(el)
    ind = Get_Indx(sr) # вывод индекса (все, что до последнего символа строки)
    # print (ind)
    lnst = Get_str(ind,el) # создание строки из заданной длины
    # print(lnst)
    back_str +=lnst
    
print(f'Восстановленная строка: \n {back_str}')



