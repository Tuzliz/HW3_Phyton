#- Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.
import random 
random_float_lst = []
for i in range(1,6):
  random_float_lst.append(round(random.uniform(1,2),2)) 
print(random_float_lst)

def min_max(random_float_lst):
    m_min = random_float_lst[0]
    m_max = random_float_lst[0]

    for i in random_float_lst:
        if i < m_min:
            m_min = i
        else:
            if i > m_max:
                m_max = i    
    return round (m_max - m_min, 2)
  
print(f'Разница между min и max значением дробной части: {min_max(random_float_lst)}') 

