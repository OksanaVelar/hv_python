# Создайте программу для игры в ""Крестики-нолики""

import task2_1

a = 3
b = 3
r = 1 

tab = [['1', '2', '3'],['4', '5', '6'],['7', '8','9']]
task2_1.Print_new_tab(tab)
print('')

gamershed = ['Gmr1','Gmr2']
print(f'Список игроков: \n   Gmr1\n   Gmr2\n')

engaged = ['0']

gmr_symb = None
num_try = None
Gmr1_0 = None
Gmr2_X = None
num_try = 0 
# print(f'Количество попыток: {num_try}') 
print('')

begin = input('Для начала игры нажмите клавишу "Enter"')
print('')

while num_try < 9:
    curr_gmr = gamershed[0]
    print(f'Право хода предоставляется игроку {curr_gmr}')
    try_gamer = input(f'Выполните ход - введите номер ячейки от 1 до 9 и нажмите "Enter"')
    check_result = task2_1.Check_step(engaged, try_gamer)
    print (check_result)
    if check_result == False:
        print('Указанная Вами ячейка уже использована. Пожалуйста, выберите другую.')
    task2_1.GAME(tab, try_gamer, curr_gmr, num_try)
    num_try += 1 
    win = task2_1.Count_for_win(tab)
    if win == True:
        print(f'Выиграл {curr_gmr}')
        break
    task2_1.Rotate_part(gamershed)
    
if win == False:
    print('Победила дружба!')



    


    




