# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# a = int(input('Введите первое число: '))
# d = int(input('Введите разность: '))
# Quantity = int(input('Введите количество элементов: '))

# for i in range(Quantity):
#     print (a + i * d, end=' ')

# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint
numN = int(input("Введите количество чисел в массиве: "))
array = [randint(0,10) for _ in range(numN)] 
print(array)

Start = int(input('Введите первое число диапазона: '))
End = int(input('Введите последнее число диапазона: '))

for i in range(len(array)):
    if Start <= array[i] <= End:
        print(i)
    
    
    