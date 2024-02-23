'''Задача: Склад с фруктами.
На складе лежат разные фрукты в разном количестве.
Нужно написать функцию total_fruits, которая на вход принимает любое количество названий фруктов и их количество, а возвращает общее количество фруктов на складе.
можно решить через *kwargs

Пример
После вашего кода будет добавлена следующая строка:
print(total_fruits(apples=10, bananas=5, oranges=8))
На выходе:
23
'''

'''
копипаста из автотестов после принятия решения платформой
'''
# Введите ваше решение ниже
def total_fruits(**fruits):
    total = 0
    for fruit, quantity in fruits.items():
        total += quantity
    return total




#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

#print(total_fruits(apples=10, bananas=5, oranges=8))


'''
идеальное решение платформы:
def total_fruits(**fruits):
    total = 0
    for amount in fruits.values():
        total += amount
    return total
'''