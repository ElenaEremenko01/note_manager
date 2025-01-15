from datetime import datetime as dt
from datetime import timedelta as td
from tabulate import tabulate
from create_note_function import create_note
from colorama import Fore, Style, init
init(autoreset= True)

print(f'Меню действий:\n1. Создать новую заметку\n2. Показать все заметки\n3. Обновить заметку\n4. Удалить заметку\n5. Найти заметки\n6. Выйти из программы')
while True:
    menu = input('Ваш выбор:')
    try:
        choice = int(menu)
        break
    except ValueError:
        print(f'{Fore.RED}{Style.BRIGHT}Ошибка!!!')
        print(f'Ответ может быть в диапазоне чисел {Fore.YELLOW} 1,2,3,4,5,6.')
        continue
    if menu == 1:
        note = create_note()
        print('Новая заметка создана')

