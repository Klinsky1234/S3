# Задача 0. Дан список, заполненный случайными
# числами от 0 до 10. Определите, является ли сумма
# всех элементов чётной.
import random  # мы подключили библиотеку


def task_0():
    days = 7
    # n = [0] * days  # мы можем умножать на длину
    # for i in range(days):
    #     n[i] = random.randint(0, 10)  # возвращает случайные числа от и до
    # print(n)
    num = [random.randint(0, 10) for el in range(days)]
    # выше строчка - это Генератор, а [] - кв.скобки это создание списков
    print(num)
    sum = 0
    for i in range(days):
        sum += num[i]
    print(f"сумма всех элементов = {sum}")
    if sum % 2 == 0:
        print("сумма чётная")
    else:
        print("сумма нечётная")


# task_0()

import random


def S3_task_1():
    # Задача 1. В списке хранятся сведения о количестве осадков, выпавших за каждый день июня.
    # Определите в какой период выпало больше осадков: в первой или второй половине июня.
    days = 30
    numb = [random.randint(0, 25) for el in range(days)]
    print(numb)
    f_sum = 0
    t_sum = 0
    for i in range(15):
        f_sum += numb[i]
    print(f_sum)
    for j in range(15, days):
        t_sum += numb[j]
    print(t_sum)
    if f_sum > t_sum:
        print("в первой половине выпало больше")
    else:
        print("во втророй половине выпало больше")


# S3_task_1()
def S3_task_1_1():
    days = 30
    numb = [random.randint(0, 25) for el in range(days)]
    f_part = numb[:15]
    t_part = numb[15:]
    # выше указаны срезы
    print(numb)
    f_sum = 0
    t_sum = 0
    # ниже цикл отщёлкает 15 раз (половину) и за 15 повторений мы набьём обе части
    for i in range(len(f_part)):
        f_sum += f_part[i]
        t_sum += t_part[i]
    print(f_sum)
    print(t_sum)
    if f_sum > t_sum:
        print("в первой половине выпало больше")
    elif f_sum < t_sum:
        print("во втророй половине выпало больше")
    else:
        print("одинаково")


S3_task_1_1()
