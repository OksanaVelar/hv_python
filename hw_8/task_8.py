# реализуйте механизм перемешивания списка
import random
num = int(input('Введите число для определения количества элементов последовательности и нажмите "Enter": '))
string = list(range(num))
print(string)
random.shuffle(string)
print(string)
