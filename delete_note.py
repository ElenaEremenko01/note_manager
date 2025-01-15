#Программа удаляет заметки на основе введённого пользователем имени пользователя или заголовка.
#Если заметка не найдена, выводится соответствующее сообщение.
#После удаления обновлённый список заметок корректно отображается.
from tabulate import tabulate
from colorama import Fore, Style, init
init(autoreset= True)
note_try1 = [{'username': 'Алексей', 'title': 'Купить продукты на неделю', 'content': 'Купить продукт на неделю'},
         {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену'},
         {'username': 'Елена', 'title': 'Книга', 'content': 'Написать книгу'}]


# запускаем цикл, с запросом удаления заметки
def delete_note(notes):
    if not notes:
        print(Fore.GREEN + Style.BRIGHT + 'Список заметок пуст')
        return notes
    else:
        print(Fore.CYAN + 'Текущий список заметок:')
        headers = ['№', 'Имя пользователя', 'Заголовок', 'Содержание']  # Собираем названия столбцов для таблицы
        table_list = []
        for i, note in enumerate(notes, 1):
            table_list.append([i, note['username'],
                               note['title'],
                               note['content']])
        print(tabulate(table_list, headers=headers, tablefmt='grid', stralign='center'))
    note_del = input(
        f'{Fore.WHITE}Введите {Style.BRIGHT}{Fore.YELLOW}ИМЯ ПОЛЬЗОВАТЕЛЯ{Style.NORMAL}{Fore.WHITE} или {Style.BRIGHT}{Fore.YELLOW}ЗАГОЛОВОК{Style.NORMAL}{Fore.WHITE} для удаления заметки:').strip().lower()
    for i in reversed(range(len(notes))):
            if notes[i]['username'].lower() == note_del:
                confirmation2 = input(f'{Fore.RED}Вы уверены, что хотите удалить заметку?{Fore.YELLOW}(да\нет)').strip().lower()
                if confirmation2 == 'да':
                    del notes[i]
                    print(Fore.GREEN + 'Заметка успешно удалена')
                    print(Fore.CYAN + 'Текущий список заметок:')
                    headers = ['№', 'Имя пользователя', 'Заголовок', 'Содержание']  # Собираем названия столбцов для таблицы
                    table_list = []
                    for j, note in enumerate(notes, 1):
                        table_list.append([j, note['username'],
                                           note['title'],
                                           note['content']])
                    print(tabulate(table_list, headers=headers, tablefmt='grid', stralign='center'))
                    break
                elif confirmation2 == 'нет':
                    print(Fore.CYAN + 'Текущий список заметок:')
                    headers = ['№', 'Имя пользователя', 'Заголовок','Содержание']  # Собираем названия столбцов для таблицы
                    table_list = []
                    for j, note in enumerate(notes, 1):
                        table_list.append([j, note['username'],
                                           note['title'],
                                           note['content']])
                    print(tabulate(table_list, headers=headers, tablefmt='grid', stralign='center'))
                    break
                else:
                    print(f'{Fore.RED}Ошибка!!!')
                    print(f'{Fore.RED}Ответ может быть {Fore.YELLOW}{Style.BRIGHT}да/нет')
            elif notes[i]['title'].lower() == note_del:
                confirmation3 = input(f'Вы уверены, что хотите удалить заметку?{Fore.YELLOW}(да\нет)').strip().lower()
                if confirmation3 == 'да':
                    del notes[i]
                    print(Fore.GREEN + 'Заметка успешно удалена')
                    print(Fore.CYAN + 'Текущий список заметок:')
                    headers = ['№', 'Имя пользователя', 'Заголовок', 'Содержание']  # Собираем названия столбцов для таблицы
                    table_list = []
                    for j, note in enumerate(notes, 1):
                        table_list.append([j, note['username'],
                                       note['title'],
                                       note['content']])
                    print(tabulate(table_list, headers=headers, tablefmt='grid', stralign='center'))
                    break
                elif confirmation3 == 'нет':
                    print(Fore.CYAN + 'Текущий список заметок:')
                    headers = ['№', 'Имя пользователя', 'Заголовок','Содержание']  # Собираем названия столбцов для таблицы
                    table_list = []
                    for j, note in enumerate(notes, 1):
                        table_list.append([j, note['username'],
                                           note['title'],
                                           note['content']])
                    print(tabulate(table_list, headers=headers, tablefmt='grid', stralign='center'))
                    break
                else:
                    print(f'{Fore.RED}Ошибка!!!')
                    print(f'{Fore.RED}Ответ может быть {Fore.YELLOW}{Style.BRIGHT}да/нет')
            else:
                print(Fore.RED + 'Заметки с такими параметрами нет')
                print(Fore.CYAN + 'Текущий список заметок:')
                headers = ['№', 'Имя пользователя', 'Заголовок', 'Содержание']  # Собираем названия столбцов для таблицы
                table_list = []
                for j, note in enumerate(notes, 1):
                    table_list.append([j, note['username'],
                                   note['title'],
                                   note['content']])
                print(tabulate(table_list, headers=headers, tablefmt='grid', stralign='center'))




delete_note(note_try1)

