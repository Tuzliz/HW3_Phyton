
#1 - Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint
lst_numbers = []
for i in range(1,7):
    lst_numbers.append(randint(1,10))
print(lst_numbers)
suma = 0
odd_num=[]
for i in range(0,len(lst_numbers)):
        if i % 2 == 0:
            odd_num.append(lst_numbers[i])
print(f'Элементы на нечетных позициях: {odd_num}')
print(f'Сумма элементов на нечетных позициях: {sum(odd_num)}')


    
                




            
    

