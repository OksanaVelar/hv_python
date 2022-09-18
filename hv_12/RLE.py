# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

# Создание нового элемента
def Get_new_symb(number, symb):
    new_symb = '%d%s' % (number, symb)
    return (new_symb)

# замена элемента в исходной строке
def Replace_sym (str, symb, sym2):
    new_str = str.replace(symb, sym2)
    return(new_str)

def Join_new_symb(symb1,symb2):
    grow_str = symb1+symb2
    return(grow_str)
# encoded_str = Join_part_str(part1,part2)
# print(encoded_str)

init_str = 'дистиллированный'
num = 1
for i in range (len(init_str)):
    new_symb = Get_new_symb(num, init_str[i])
    new_str = Replace_sym (init_str, init_str[i], new_symb)
        
    print(new_str)
        
    # elif init_str[i] == init_str[i+1]:
    #     num = num+1
    #     new_symb = Get_new_symb(num, init_str[i])
    #     uncoded_str = init_str.replace(init_str[i], new_symb)
    #     uncoded_str = init_str.replace(init_str[i+1], '')
   


# print(uncoded_str)


# Соединение пар в закодированную строку
# part1 = "4";
# part2 = "8";

# def Join_new_symb(symb):
#     grow_str = symb+symb
#     return(grow_str)
# encoded_str = Join_part_str(part1,part2)
# print(encoded_str)
