# 4 - Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#*Пример:*

#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10
def num_biger_then_zero(text):

    int_num = True
    while int_num:
        n = input(f"{text}")
        if n.isdigit():
            n = int(n)
            if n <= 0:
                print("Введите число > 0")
            else:
                int_num = False
        else :
            print("Не число, попробуйте еще раз")
    return n
n = num_biger_then_zero("Введите n : ") 
ost = ''  
while n > 0:  
    ost = str(n % 2) + ost 
    n = n // 2 

print(f'Двоичное число: {ost}')