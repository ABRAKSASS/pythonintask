# Задача 6. Вариант 7.
# Создайте игру, в которой компьютер загадывает имя одного из двух сооснователей компании
# Google, а игрок должен его угадать.

# Lysenko N.A.
# 23.03.2017

import random

#Сергей Брин и Ларри Пейдж - основатели гугл

Makers = [
    "Сергей Брин",
    "Лари Пейдж"
]

pick = random.choice(Makers)
maker = input("Назовите одного из двух основателей компании Google: ")

if pick == maker:
    print("\nВы угадали, компьютер загадал: ", pick)
else:
    print("\nВы не угадали, компьютер загадал: ", pick)

input ('\nНажмите Enter для выхода.') 
