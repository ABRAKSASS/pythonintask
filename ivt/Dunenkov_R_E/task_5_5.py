# Задача 5 Вариант 5
# Напишите программу, которая бы при запуске случайным образом отображала название одного из восьми соборов Московского кремля.

# Дуненков Р.Е.
# 05.04.2017.

import random
print('Программа случайным образом отображает название одного из восьми соборов Московского кремля')
feat = random.randint(1,8)
print('собор Московского кремля', end=" ")
if feat == 1 :
    print("Собор первый: Успенский")
elif feat == 2 :
    print("Собор второй: Благовещенский")
elif feat == 3 :
    print("Собор третий: Архангельский")
elif feat == 4 :
    print("Собор четвертый: храм Положения ризы Божией Матери во Влахерне")
elif feat == 5 :
    print("Собор пятый: Патриарший дворец")
elif feat == 6 :
    print("Собор шестой: Двенадцати апостолов")
elif feat == 7 :
    print("Собор седьмой: Верхоспасский собор")
elif feat == 8 :
    print("Собор восьмой: Церковь Рождества Богородицы на Сенях")
 
input("\n\nНажмите Enter для выхода.") 