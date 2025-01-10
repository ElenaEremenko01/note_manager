from datetime import datetime as dt
from datetime import date
from datetime import timedelta as td

# создаем функцию для создания заметки и запроса данных у пользователя, возвращаем функцию в виде словаря
def create_note():
    print('Добро пожаловать в "Менеджер заметок"! Вы можете добавить новую заметку.')
    # запрашиваем данные для заметки у пользователя вставляем
    username = input('Введите имя пользователя:')
    while True:# если пользователь оставит поле пустым, цикл с запросом имени повторится
        if username == '' or username == ' ':
            print('Поле "Имя пользователя не может быть пустым"')
            username = input('Введите имя пользователя:')
        else:
            break
    title = input('Введите заголовок:')# если пользователь оставит поле пустым, цикл с запросом имени повторится
    title_list = [title]
    if title == '' or title == ' ':
        print('Заголовок не может быть пустым')
        title = input('Введите заголовок:')
    while True: # запускаем цикл для введения нескольких заметок, цикл прервется словом "Стоп"
        title = input('Введите еще один заголовок или введите "стоп"/нажмите Enter для завершения:').lower()
        title_list.append(title)
        unique_titles = list(set(title_list))# выводим уникальные значения при помощи множества
        if title == 'стоп' or title == '':
            for i in unique_titles[::-1]:
                if i == 'стоп' or i == '':
                    unique_titles.remove(i)
                    unique = ','.join(unique_titles)
            break
    content = input('Опишите заметку:') # если пользователь оставит поле пустым, цикл с запросом имени повторится
    while True:
        if content == '' or content == ' ':
            print('Поле "Имя пользователя" не может быть пустым"')
            content = input('Введите имя пользователя:')
        else:
            break

    possible_statuses = ["выполнено", "в процессе", "новая"] # создаем список с возможными статусами
    status = input("Введите текущий статус заметки: (выполнено, в процессе, новая)").lower()
    while status not in possible_statuses: # Если пользователь введет неверный статус, выйдет предупредительное сообщение и цикл повторится
        print('Статус введен неправильно.Введите корректный статус')
        status = input("Введите текущий статус заметки: (выполнено, в процессе, новая)")

    created_date = dt.now().strftime('%d.%m.%Y')# выводим текущую дату в нужном формате

    issue_date = input('Введите дату истечения заметки (дедлайн) в формате (дд.мм.гггг):')
    while True:
        if issue_date == '' or issue_date == ' ': # если поле будет пустым по умолчанию к текущей дате добавится 14 дней
            temp_date = dt.now() + td(days=14)
            issue_date = temp_date.strftime('%d.%m.%Y')
        try:
            issue_date = dt.strptime(issue_date, '%d.%m.%Y').date()
            break
        except ValueError:
            print(f'Дэдлайн нужно ввести в формате: дд.мм.гггг (Например: 26.12.2000)')
        issue_date = input('Введите дату дедлайна в формате (дд.мм.гггг):')
    #Собираем данные заметки в словарь
    note = {'Имя пользователя': username,
        'Заголовок': unique,
        'Содержание': content,
        'Статус': status,
        'Дата создания заметки': created_date,
        'Дата истечения заметки': issue_date.strftime('%d.%m.%Y')}
    return note # Возвращаем функцию в виде словаря


print(f'Заметка создана: {create_note()}')