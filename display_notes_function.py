from datetime import datetime as dt
from colorama import Fore, Style, init
init(autoreset=True)# сбрасываем стиль, чтобы цвета в цикле не повторялись
#Создаем функцию для отображения заметок
def display_notes(note_list):
    # Для пустого списка
    if not note_list:
        print(Fore.GREEN +'Копировать код')
        print(Fore.GREEN + 'У вас нет сохранённых заметок')
    if note_list:
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
                if choice_for_sorted == 'да':
                    sorted_data = sorted(note_list, key=lambda x: dt.strptime(x['Дата истечения заметки'], '%d.%m.%Y'))
                else:
                    sorted_data = note_list
                 # Цикл для отображения укороченного списка заметок с использованием цветов
                for i, note in enumerate(sorted_data, 1):
                    print(f'{Fore.MAGENTA}Заметка №{i}.')
                    print(f'{Style.BRIGHT}Имя пользователя: {note["Имя пользователя"]}')
                    print(f'{Style.BRIGHT}Заголовок заметки: {note["Заголовок"]}')
                    print('_______________')
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
                    sorted_data = sorted(note_list, key=lambda x: dt.strptime(x['Дата истечения заметки'], '%d.%m.%Y'))
                else:
                    sorted_data = note_list
                # Цикл для отображения удлененного списка заметок с использованием цветов
                for i, note in enumerate(sorted_data, 1):
                    print(f'{Fore.MAGENTA}Заметка №{i}.')
                    print(f'{Style.BRIGHT}Имя пользователя: {note["Имя пользователя"]}')
                    print(f'{Style.BRIGHT}Заголовок заметки: {note["Заголовок"]}')
                    print(f'{Style.BRIGHT}Описание заметки: {note['Содержание']}')
                    print(f'{Style.BRIGHT}Статус заметки: {note["Статус"]}')
                    print(f'{Style.BRIGHT}Дата создания заметки: {note["Дата создания заметки"]}')
                    print(f'{Style.BRIGHT}Дата истечения заметки: {note["Дата истечения заметки"]}')
                    print('_______________')
                break
             # обработка ошибок
            else:
                print(f'{Style.BRIGHT}{Fore.RED}Ошибка!!!')
                print(f'{Fore.RED}Ответ может быть:{Style.BRIGHT}Заголовки/Полные данные')

notes = [{'Имя пользователя': 'Алексей',
              'Заголовок': 'Список покупок',
              'Содержание': 'Купить продукты на неделю',
              'Статус': 'новая',
              'Дата создания заметки': '28.11.2024',
              'Дата истечения заметки': '30.11.2024'}, {'Имя пользователя': 'Маша',
              'Заголовок': 'Список покупок',
              'Содержание': 'Купить продукты на неделю',
              'Статус': 'новая',
              'Дата создания заметки': '27.11.2024',
              'Дата истечения заметки': '01.11.2024'}]


display_notes(notes)
