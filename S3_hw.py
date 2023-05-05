import time

# Задача 1. Создайте список. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8

# N = int(input("Enter number: "))


# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)


# list_1 = []
# for i in range(1, (N + 1)):
#     list_1.append(fib(i))
# print(*list_1)

# Задача 2. В списке находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.


def S3_hw2():
    fruits = {"а": "абрикос, ананас, авокадо", "б": "банан", "в": "вишня"}
    n = input("Введите первую букву фрукта: ").lower()
    #     for k, v in fruits.items():
    if n in fruits:
        print(fruits[n])
    else:
        print("такого фрукта нет :-( ")


# S3_hw2()


# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре.
# Бот должен, как минимум, отвечать на фразы «привет»,
# «как тебя зовут». Если фраза ему неизвестна, он выводит соответствующую фразу.
def S3_hw3():
    script = {
        "привет": "Привет, человек!",
        "как тебя зовут?": "Меня зовут бот-Димас",
        "погода": "зайди на https://www.gismeteo.ru/ и посмотри сам, я тебе не Павел Глоба! ",
        "в": f"Текущее время: {time.ctime()}",
    }

    question = input("Задайте вопрос или напишите привет: ")
    question = question.lower()

    if question in script:
        print(script[question])
    else:
        print("кожанный, твоя - моя не понимай!")
