from datetime import datetime as dt
from colorama import Fore, Style, init
from tabulate import tabulate
init(autoreset= True)# сбрасываем стиль, чтобы цвета в цикле не повторялись
#Создаем функцию для отображения заметок
def display_notes(note_list):
    # Для пустого списка, возвращает список
    if not note_list:
        print(Fore.GREEN +'Копировать код')
        print(Fore.GREEN + 'У вас нет сохранённых заметок')
        return note_list

    #Цикл для запроса способа отображения заметок
    while True:
        choice_for_display = input(f'Вывести только заголовки заметок или полные данные?{Style.BRIGHT} {Fore.CYAN}(Заголовки/Полные данные):').strip().lower()
        if choice_for_display == 'заголовки':
            while True:
                # цикл для сортировки данных по дэдлайну
                choice_for_sorted = input(f'Желаете отсортировать заметки по дате дэдлайна?{Style.BRIGHT} {Fore.CYAN}(да\нет):').strip().lower()
                if choice_for_sorted in ['да', 'нет']:
                    break
                # Обработка ошибок
                else:
                    print(Fore.RED + Style.BRIGHT+'Ошибка!!!')
                    print(f'{Fore.RED}Ответ может быть:{Style.BRIGHT}{Fore.RED} да\нет')
            # Сортировка по дате дэдлайна
            if choice_for_sorted == 'да':
                sorted_data = sorted(note_list, key=lambda x: dt.strptime(x['issue_date'], '%d.%m.%Y'))
            else:
                sorted_data = note_list
                # Цикл для отображения укороченного списка заметок с использованием таблицы
            headers = ['№', 'Имя пользователя', 'Заголовок'] #Собираем названия столбцов для таблицы
            table_list = []# Создаем пустой список для того, чтобы сюда добавить содержание после enumerate(выведет кортеж)
            for i, note in enumerate(sorted_data, 1):
                table_list.append([i, note["username"], note["title"]] )
            print(tabulate(table_list, headers= headers, tablefmt='grid', stralign='center'))
            break
        elif choice_for_display == 'полные данные':
            while True:
                choice_for_sorted = input(f'Желаете отсортировать заметки по дате дэдлайна?{Style.BRIGHT}{Fore.CYAN}(да\нет)').strip().lower()
                if choice_for_sorted in ['да', 'нет']:
                    break
                else:
                    print(Fore.RED + Style.BRIGHT + 'Ошибка!!!')
                    print(f'{Fore.RED}Ответ может быть: {Style.BRIGHT}{Fore.RED}да\нет')
            if choice_for_sorted == 'да':
                sorted_data = sorted(note_list, key=lambda x: dt.strptime(x['issue_date'], '%d.%m.%Y'))
            else:
                sorted_data = note_list
            # Цикл для отображения удлиненного списка заметок с использованием цветов
            headers = ['№', 'Имя пользователя', 'Заголовок', 'Содержание', 'Статус', 'Дата создания заметки', 'Дата истечения заметки']  # Собираем названия столбцов для таблицы
            table_list = []
            for i, note in enumerate(sorted_data, 1):
                table_list.append([i, note['username'],
                                       note['title'],
                                       note['content'],
                                       note['status'],
                                       note['created_date'],
                                       note['issue_date']])
            print(tabulate(table_list, headers= headers, tablefmt='grid', stralign='center'))# разделяем каждую заметку в таблице чертой и выравниваем по центру
            break
            # обработка ошибок
        else:
            print(f'{Style.BRIGHT}{Fore.RED}Ошибка!!!')
            print(f'{Fore.RED}Ответ может быть:{Style.BRIGHT}Заголовки/Полные данные')

test_notes = [
        {"username": "Алексей", "title": "Список покупок", "content": "Купить продукты на неделю", "status": "новая", "created_date": "27.11.2024", "issue_date": "30.11.2024"},
        {"username": "Мария", "title": "Учеба", "content": "Подготовиться к экзамену", "status": "в процессе", "created_date": "25.11.2024", "issue_date": "01.12.2024"},
        {"username": "Иван", "title": "Работа", "content": "Закончить отчёт", "status": "в процессе", "created_date": "20.11.2024", "issue_date": "28.11.2024"},
        {"username": "Ольга", "title": "Здоровье", "content": "Записаться к врачу", "status": "новая", "created_date": "18.11.2024", "issue_date": "23.11.2024"},
        {"username": "Дмитрий", "title": "Отпуск", "content": "Собрать документы", "status": "новая", "created_date": "15.11.2024", "issue_date": "20.11.2024"},]


display_notes(test_notes)
