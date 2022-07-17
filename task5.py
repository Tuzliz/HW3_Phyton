# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# # *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] # F−n = (−1)^(n+1)*F(n).

def fib(n):
    if (n <= 1):
        return n
    else:
        return (fib(n-1) + fib(n-2))
n = int(input("Введите число последовательности n:"))
#print("Положительное Фибоначчи:")
positive_lst=[]
for i in range(n):
    # print(fibonacci(i))
    positive_lst.append(fib(i))
print(f'Положительное Фибоначчи: \n{positive_lst}')
negative_lst =[]
my_lst = positive_lst
for i in range(1, len(my_lst)):
    negative_lst.append(my_lst[i]*((-1)**(i+1)))

negative_lst.reverse()

print(f'Отрицательное Фибоначчи: \n{negative_lst + my_lst}')
# F−n = (−1)^(n+1)*F(n).
