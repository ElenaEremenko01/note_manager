from datetime import datetime as dt
from datetime import timedelta as td
from tabulate import tabulate
# импортируем, ранее созданные функции
from create_note_function import create_note
from display_notes_function import display_notes
from update_note_function import update_note
from delete_note import delete_note
from search_notes_function import search_notes

from colorama import Fore, Style, init
init(autoreset= True)
# создаем цикл для отображения меню
while True:
    print(f'Меню действий:\n1. Создать новую заметку\n2. Показать все заметки\n3. Обновить заметку\n4. Удалить заметку\n5. Найти заметки\n6. Выйти из программы')
    menu = input(f'{Fore.CYAN}{Style.BRIGHT}Ваш выбор:')
    # В случае неверного ввода, будет обработана ошибка
    try:
        choice = int(menu)
    except ValueError:
        print(f'{Fore.RED}{Style.BRIGHT}Ошибка!!!')
        print(f'Ответ может быть в диапазоне чисел {Fore.YELLOW} 1,2,3,4,5,6.')
        continue
    #Создаем условия для каждого выбора пользователя
    if choice == 1:
        note = create_note()# Вызываем функцию создания
        create_list = []
        print(f'{Fore.GREEN}{Style.BRIGHT}Новая заметка создана')
        create_list.append(note)# собираем словари в список для дальнейшей обработки
    elif choice == 2:# вызываем функцию отображения, куда вкладываем список созданный в create_note
        display_note = display_notes(create_list)
    elif choice == 3:# вызываем функцию обновления заметок, куда передаем словарь из функции create_note
        updating = update_note(note)
    elif choice == 4:# вызываем функцию удаления, куда вкладываем список созданный в create_note
        deletion = delete_note(create_list)
    elif choice == 5:# вызываем функцию для поиска заметок, куда вкладываем список созданный в create_note
        keyword_for_search = str(input('Введите ключевое слово').strip().lower())
        status_for_search = str(input('Введите статус заметки').strip().lower())
        searching = search_notes(create_list, keyword_for_search, status_for_search)
    elif choice == 6:# цикл завершиться при выборе 6
        print('Программа завершена. Спасибо за использование!')
        break
    else:# если пользователь введет неверные данные
        print(f'{Fore.RED}{Style.BRIGHT}Ошибка!!!')
        print(f'Ответ может быть в диапазоне чисел {Fore.YELLOW} 1,2,3,4,5,6.')


