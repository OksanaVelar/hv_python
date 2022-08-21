from collections import Counter
h_shed1 = ['X','X','r']
counter = None
tab = [['1', '2', '3'],['X', 'X', 'X'],['7', '8','9']]
# def Count(y):
#     counter = Counter(y)
#     print(counter)
#     return(counter)
# Count(h_shed1)
# print(list(h_shed1))
# print(len(h_shed1))

# o = None
# def Count(h_shed1):
#     for i in range (len(h_shed1)):
#         counter = h_shed1.count(X')
#         o = counter
#     print(o)

#     return(o)
# Count(h_shed1)

def Count_for_line(tab):
    for i in range(3):
        if tab[i][0] == tab[i][1] and tab[i][1] == tab[i][2]:
            print('Победа')
Count_for_line(tab)