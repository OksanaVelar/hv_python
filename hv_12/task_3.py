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

sweets = 106
max = 28
Gamershed = ['Gmr1','Gmr2']
winner = None
print(f'Список игроков: \n   Gmr1\n   Gmr2')
first_stp = (input('Для проведения жеребьевки нажмите клавишу "Enter". Жеребьевка будет осуществлена автоматически:\n'))

for i in range (len(Gamershed)):
    first_gamer = random.choice(Gamershed)
print(f'Право первого хода предоставляется игроку {first_gamer}')

def Show_winner(shed):
    for i in range (len(shed)):
        # shed.reverse()
        winner = shed[i-1]
    return(winner)

def sub(x,y):
    balance = x-y
    return(balance)

while sweets > max:
    number = int(input('Выполните ход - введите число от 1 до 28, не превышающее остаток и нажмите "Enter"\n '))
    if number <= max and number != 0:
        sweets = int(sub(sweets,number))
        print(f'Осталось конфет: {sweets}\n')
        winner = Show_winner(Gamershed)
    elif number == 0:
        print('Ход не выполнен. Для выполнения хода необходимо ввести число не менее 1')
    elif number > max:
        print('Ход не выполнен. Для выполнения хода необходимо ввести число, не превышающее остаток')
print(f'Победитель - {winner}')




