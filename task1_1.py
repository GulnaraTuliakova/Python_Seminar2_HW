# 1. #Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Решение со строкой
    
def func_2 (num:str): 
    num = num.replace('.','')
    summ = 0
    for i in num:
        summ += int(i)
        
    return (summ)

x = input('Введите дробное число с точкой в виде разделителя: ')   
print(f'Сумма цифр в числе - {func_2(x)}')

