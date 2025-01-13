from colorama import Fore, Style, init
from tabulate import tabulate
init(autoreset=True)# сбрасываем стиль, чтобы цвета в цикле не повторялись
# Создаем функцию для поиска заметок
def search_notes(notes, keyword=None, status=None):
    # Если заметок нет, то выйдет сообщение об отсутствии и функция вернет список
    if not notes:
        print(Fore.GREEN + 'Копировать код')
        print(Fore.GREEN + 'Нет текущих заметок')
        return notes
    # Если пользователь не укажет параметры для поиска, то функция вернет список
    if keyword is None and status is None:
        return notes
    # Создаем пустой список, куда будем собирать подходящие заметки
    matching_list = []
    # В цикле проходимся по всем заметкам в списке
    for note in notes:
        # Создаем переменную, которая проверяет поиск по ключевому слову по ключам username, title, content
        keyword_match = (keyword is None or # Если ключевое слово не задано
                         keyword.lower() in note['username'].lower() or
                         keyword.lower() in note['title'].lower() or
                         keyword.lower() in note['content'].lower())
        # Создаем переменную, которая проверяет поиск по статусу, по ключу status
        status_match = (status is None or # Если статус не задан
                        note['status'].lower() == status.lower())
        # Создаем условие, если найдено и ключевое слово и статус, то мы добавляем заметки в пустой список
        if keyword_match and status_match:
            matching_list.append(note)
    # Если список пуст, то значит в цикле не найдено ни ключевого слова, ни статуса
    if not matching_list:
        print(f'{Fore.RED}{Style.BRIGHT}Заметки, с данными параметрами, не найдены')
        return []
    else:
        headers = ['№', 'Имя пользователя', 'Заголовок', 'Содержание', 'Статус', 'Дата создания заметки',
                   'Дата истечения заметки']  # Собираем названия столбцов для таблицы
        table_list = []
        for i, note in enumerate(matching_list, 1):
            table_list.append([i, note['username'],
                               note['title'],
                               note['content'],
                               note['status'],
                               note['created_date'],
                               note['issue_date']])
        print(tabulate(table_list, headers=headers, tablefmt='grid', stralign='center'))
        return matching_list


test_note = [
        {"username": "Алексей", "title": "Список покупок", "content": "Купить продукты на неделю", "status": "новая", "created_date": "27.11.2024", "issue_date": "30.11.2024"},
        {"username": "Мария", "title": "Учеба", "content": "Подготовиться к экзамену", "status": "в процессе", "created_date": "25.11.2024", "issue_date": "01.12.2024"},
        {"username": "Иван", "title": "Работа", "content": "Закончить отчёт", "status": "в процессе", "created_date": "20.11.2024", "issue_date": "28.11.2024"},
        {"username": "Ольга", "title": "Здоровье", "content": "Записаться к врачу", "status": "новая", "created_date": "18.11.2024", "issue_date": "23.11.2024"},
        {"username": "Дмитрий", "title": "Отпуск", "content": "Собрать документы", "status": "новая", "created_date": "15.11.2024", "issue_date": "20.11.2024"},]

keyword_for_search = str(input('Введите ключевое слово').lower())
status_for_search = str(input('Введите статус заметки').lower())

search_notes(test_note, keyword_for_search,status_for_search)

