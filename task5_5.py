# 5. Реализуйте алгоритм перемешивания списка.
# Решение c функцией

def mix_num (n):
    # n = int(input('Введите число N для создания списка: '))
    a = list(range(-n,n+1))
    b = a
    print('Список:',a)
    for i in b:
        temp = b[i]
        b[i] = b[i-1]
        b[i-1] = temp
    print ('Перемешанный список: ', b)


m = int(input('Введите число N для создания списка: '))
mix_num (m)