"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv
from pathlib import Path

target_file = Path('files/personal.csv')
personal = [
    {'name': 'Vasy', 'age': 21, 'job': 'Hairdresser'},
    {'name': 'Pety', 'age': 68, 'job': 'Conductor'},
    {'name': 'Nina', 'age': 19, 'job': 'Miner'},
    {'name': 'Ivan', 'age': 45, 'job': 'Deputy'},
    {'name': 'Galy', 'age': 19, 'job': 'Chief Executive'},
    {'name': 'Juli', 'age': 32, 'job': 'Resuscitator', 'salary': 90000},
]


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open(target_file, 'w', encoding='utf-8') as csv_file:
        head = ['name', 'age', 'job', 'salary']
        writer = csv.DictWriter(csv_file, head, delimiter=';')
        writer.writeheader()
        for man in personal:
            writer.writerow(man)


if __name__ == '__main__':
    main()
