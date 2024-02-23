'''Задача: Найдите выручку компании.
Найдите выручку компании в зависимости от месяца Для этого напишите функцию calc_income_by_month(),
которая на вход принимает список с датами и список с выручкой,
а на выходе словарь, где ключи - это месяцы, а значения - это выручка. Используйте аннотирование типов.

Пример
На входе:
dates = ['2021-11-01']
incomes = [100]
После вашего кода будет автоматически добавлено:
print(calc_income_by_month(dates = ['2021-11-01'], incomes = [100]))
На выходе:
{'11': 100}
'''

'''
копипаста из автотестов после принятия решения платформой
'''
#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

#dates = ['2021-11-01']
#incomes = [100]

# Введите ваше решение ниже
from typing import List

def calc_income_by_month(dates: List[str], incomes: List[int]) -> dict:
    income_by_month = {}
    for date, income in zip(dates, incomes):
        month = date.split('-')[1]
        if month in income_by_month:
            income_by_month[month] += income
        else:
            income_by_month[month] = income
    return income_by_month





#print(calc_income_by_month(dates = ['2021-11-01'], incomes = [100]))

'''
идеальное решение платформы:
def calc_income_by_month(dates, incomes):
    income_by_month = {}

    for i in range(len(dates)): 
        month = dates[i].split('-')[1]
        if month in income_by_month:
            income_by_month[month] += incomes[i]
        else:
            income_by_month[month] = incomes[i]

    return income_by_month
'''