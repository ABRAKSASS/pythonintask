# Задача 8. Вариант 10.
# Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4) так, чтобы к каждому слову полагалась подсказка. 
# Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений. 
# Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.

# Lisyanskaya A.V.
# 03.04.2017

import random
WORDS = ("месяц", "машина", "весло", "краски", "солнце", "собака", "лес", "шашлык", "природа", "квартира")
word = random.choice(WORDS)
correct = word
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble = jumble + word[position]
    word = word[:position] + word[(position + 1):]

print(
"""
             Добро пожаловать в игру "Анаграммы"!
         Надо переставить буквы так, чтобы получилось осмысленное слово.
        (Для выхода нажмите Enter, не вводя своей версии.)
"""
)
print("Вот анаграмма: ", jumble)
guess = input("\nПопробуйте отгадать исходное слово: ")
ball = 0
while guess != correct and guess != "":
    print("К сожалению, Вы не правы.")
    print("Если у Вас нет предположений, возьмите подсказку.")
    print("Для открытия первой буквы нажмите '1'.")
    print("Для открытия второй буквы нажмите '2'.")
    print("Для открытия последней буквы нажмите '0'.")
    guess = input("\nПопробуйте отгадать исходное слово либо используйте подсказку: ")
    if guess == '1':
        print("Первая буква исходного слова -", correct[0])
        ball = ball - 100
        guess = input("Попробуй отгадать слово: ")
    elif guess == '2':
        print("Вторая буква исходного слова -", correct[1])
        ball = ball - 100
        guess = input("Ну теперь уже легче. Попробуй отгадать слово: ")
    elif guess == '0':
        print("Последняя буква исходного слова -", correct[-1])
        ball = ball - 100
        guess = input("Ну что, теперь отгадешь? Твой ответ: ")
    ball = ball - 100
if guess == correct:
    print("Да, именно так! Вы отгадали!")
    ball = ball + 1000
    print("Вы набрали", ball, "баллов.")
print("\nСпасибо за игру!")
input("\n\nНажмите Enter, чтобы выйти.")