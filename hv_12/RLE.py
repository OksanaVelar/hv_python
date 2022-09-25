# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

# Формирование длины среза
def Cut_len(spsk):
    cut_len = spsk[:-1]
    return cut_len
    
# Создание закодированной строки
def Uncode_parts(stroka):
    i = 0
    count = 1
    new_stroka = ''   
    for i in range (len(stroka)-1):
        
        if stroka[i]==stroka[i+1]:
            count+=1
        
        else:
            new_stroka += '%d%s' % (count,stroka[i])
            count = 1

        if i == (len(stroka)-2):
            new_stroka += '%d%s' % (count,stroka[i])
    
    return new_stroka
    
original = 'AAAytttt'
uncoded = Uncode_parts(original)
print (uncoded)

