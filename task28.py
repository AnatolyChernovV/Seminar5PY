# Задача 28: Напишите рекурсивную функцию 
# sum(a, b), возвращающую сумму двух целых 
# неотрицательных чисел. Из всех арифметических 
# операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

def sum(a, b):
    if b == 0:
        return a
    return sum(a, b - 1) + 1

n = int(input())
m = int(input())
print(sum(n, m))
