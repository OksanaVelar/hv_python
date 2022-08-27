
import random

def Print_matrix(matr):
    for m in matr:
        for s in m:
            print(s, end='|')
        print()
        print('------')



def User_go(matr, user_symbol):
    a = int(input('Введите координату x: '))
    b = int(input('Введите координату y'))
    matr[a][b] = user_symbol
    return matr

def symbol_choice(user):
    if user == False:
        user_symbol = 'X'
    else:
        user_symbol = '0'
    return user_symbol

def Check_win(matr):
    result = False
    for m in matr:
        if m[0] == m[1] and m[0] == m[2] and m[0] != ' ':
            result = True
            break
        else:
            continue
    
    for j in range(3):
        if matr[0][j] == matr[1][j] and matr[0][j] == matr[2][j] and matr[0][j] != ' ':
            result = True
            break
        else:
            continue

    if matr[0][0] == matr[1][1] and matr[0][0] == matr[2][2] and matr[0][0] != ' ':
        result =  True
    elif matr[0][2] == matr[1][1] and matr[0][2] == matr[2][0] and matr[0][2] != ' ':
        result = True

    return result
            

fer = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
Print_matrix(fer)

player = random.choice([True,False])
flag = False
for i in range(9):
    if player == True:
        print('Ходит игрок 1.')
        player_symbol = 'X'
        User_go(fer, player_symbol)
        flag = Check_win(fer)
        if flag == True:
            print('Победил игрок 1!!!')
            break
        Print_matrix(fer)
        player-=1
        continue
    else:
        print('Ходит игрок 2.')
        player_symbol = '0'
        User_go(fer, player_symbol)
        flag = Check_win(fer)
        Print_matrix(fer)
        if flag == True:
            print('Победил игрок 2!!!')
            break
        player+=1
        continue