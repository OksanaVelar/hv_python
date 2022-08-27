
gamershed = ['Gmr1', 'Gmr2']
try_gamer = None

# закрепление символов за игроками РАБОТАЕТ
def Sym_Game(curr_gamer):
    if curr_gamer == 'Gmr1':
        gamer_symb = 'O'
    else:
        gamer_symb = 'X'

    return(gamer_symb)

# ротация игроков РАБОТАЕТ
def Rotate_part(shed):
    shed.reverse()
    return(shed)

# чек корректного ввода

def Check_step(zzz, try_gamer):
    check_result = True
    for i in range (len(zzz)):
        if zzz[i] == try_gamer:
            check_result = False
    return(check_result)
    

# заполнение таблицы по ходу игры РАБОТАЕТ
num_try = 0
def GAME(spsk, try_gamer, curr_gamer, num_try, vvv):
    for i in range(len(spsk)):
        for j in range(len(spsk)):
            if spsk[i][j] == try_gamer:
                spsk[i][j] = Sym_Game(curr_gamer)
                num_try += 1   
                vvv.append(try_gamer)
                # try_gamer = 0
        
    print(f'Ход номер {num_try}')
    print(f'Номера использованных ячеек: {vvv}')
    Print_new_tab(spsk)
    print('')


def Count_for_win(tab):
    flag = False
    for i in range(3):
        if tab[i][0] == tab[i][1] and tab[i][1] == tab[i][2]:
            flag = True
        elif tab[0][i] == tab[1][i] and tab[1][i] == tab[2][i]:
            flag = True
        elif tab[0][i] == tab[1][1] and tab[1][1] == tab[2][2]:
            flag = True
        elif tab[2][0] == tab[1][1] and tab[1][1] == tab[0][2]:
            flag = True
        
    return(flag)

# Вывод таблицы с результатами выполненных ходов РАБОТАЕТ

def Print_new_tab(spsk):
    for s in spsk:
        print(s)
    return(spsk)
