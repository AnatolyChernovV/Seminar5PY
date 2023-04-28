# Задача 26:  Посчитать факториал (произведение 1 до N)
# и треугольное число (сумма чисел от 1 до N)
# для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов

def fact(number):
    if number == 1:
        return 1
    # return fact(number - 1) * number #факториал
    # return fact(number - 1) + number #треугольное число

N = int(input())
print(fact(N))