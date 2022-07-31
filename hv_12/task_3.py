# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты 
# у своего конкурента?
#    a) Добавьте игру против бота
#    b) Подумайте как наделить бота ""интеллектом""

import random

sweets = 100
max = 28
gamershed = ['Gmr1','Gmr2']
winner = None
game = True
print(f'Список игроков: \n   Gmr1\n   Gmr2')
first_stp = (input('Для проведения жеребьевки нажмите клавишу "Enter". Жеребьевка будет осуществлена автоматически:\n'))
# currgmr = None

for i in range (len(gamershed)):
    first_gamer = random.choice(gamershed)
    # currgmr = first_stp
print(f'Право первого хода предоставляется игроку {first_gamer}')

def Show_winner(shed):
    for i in range (len(shed)):
        if game == True:
            winner = shed[i-1]
        elif game == False:
            # shed.reverse()
            winner = shed[i]
    return(winner)

def sub(x,y):
    balance = x-y
    return(balance)

while sweets > max:
    number = int(input('Выполните ход - введите число от 1 до 28, не превышающее остаток и нажмите "Enter"\n '))
    if number <= max and number != 0:
        sweets = int(sub(sweets,number))
        print(f'Осталось конфет: {sweets}\n')
        winner = Show_winner(gamershed)
    elif number == 0:
        game = False
        winner = Show_winner(gamershed)
        print('Ход не выполнен. Для выполнения хода необходимо ввести число не менее 1')
    elif number > max:
        game = False
        winner = Show_winner(gamershed)
        print('Ход не выполнен. Для выполнения хода необходимо ввести число, не превышающее остаток')
print(f'Победитель - {winner}')


# КОД ДЛЯ БОТА:
# sweets = 100
# max = int(28)
# gamershed = ['Gmr1','mach']
# winner = None
# game = True
# # autostep = None
# print(f'Список игроков: \n   Gmr1\n   mach')
# first_stp = (input('Для проведения жеребьевки нажмите клавишу "Enter". Жеребьевка будет осуществлена автоматически:\n'))

# for i in range (len(gamershed)):
#     first_gamer = random.choice(gamershed)
#     # currgmr = first_stp
# print(f'Право первого хода предоставляется игроку {first_gamer}')

# def Choose_step (gamershed):
#     for i in gamershed:
#         if first_gamer == gamershed[i+1]:
#             step = int(random.randint(1,29)) # autostep 
#         elif first_gamer == gamershed[i]:
#             step = int(input('Выполните ход - введите число от 1 до 28, не превышающее остаток и нажмите "Enter"\n ')) # humanstep
#     return(step)    

# def Show_winner(shed):
#     for i in range (len(shed)):
#         if game == True:
#             winner = shed[i-1]
#         elif game == False:
#             # shed.reverse()
#             winner = shed[i]
#     return(winner)

# def sub(x,y):
#     balance = x-y
#     return(balance)

# while sweets > max:
#     step = Choose_step(gamershed)
#     print (step)
#     if step <= max and step != 0:
#         sweets = int(sub(sweets,step))
#         print(f'Осталось конфет: {sweets}\n')
#         winner = Show_winner(gamershed)
#     elif step == 0:
#         game = False
#         winner = Show_winner(gamershed)
#         print('Ход не выполнен. Для выполнения хода необходимо ввести число не менее 1')
#     elif step > max:
#         game = False
#         winner = Show_winner(gamershed)
#         print('Ход не выполнен. Для выполнения хода необходимо ввести число, не превышающее остаток')
# print(f'Победитель - {winner}')



