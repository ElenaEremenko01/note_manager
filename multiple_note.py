from datetime import datetime as dt
from datetime import date

# создаем функцию для создания заметки и запроса данных у пользователя, возвращаем функцию в виде словаря
def create_note():
    print('Добро пожаловать в "Менеджер заметок"! Вы можете добавить новую заметку.')
    # запрашиваем данные для заметки у пользователя
    username = input('Введите имя пользователя:')
    while True:
        if username == '' or username == ' ':
            print('Поле "Имя пользователя не может быть пустым"')
            username = input('Введите имя пользователя:')
        else:
            break
    title = input('Введите заголовок:')
    title_list = [title]
    if title == '' or title == ' ':
        print('Заголовок не может быть пустым')
        title = input('Введите заголовок:')
    while True:
        title = input('Введите еще один заголовок или введите "Стоп"/нажмите Enter для завершения:')
        title_list.append(title)
        unique_titles = list(set(title_list))
        if title == 'Стоп' or title == 'стоп' or title == '':
            for i in unique_titles[::-1]:
                if i == 'Стоп' or i == 'стоп' or i == '':
                    unique_titles.remove(i)
                    unique = ','.join(unique_titles)
            break
    content = input('Опишите заметку:')
    while True:
        if content == '' or content == ' ':
            print('Поле "Имя пользователя не может быть пустым"')
            content = input('Введите имя пользователя:')
        else:
            break

    possible_statuses = ["выполнено", "в процессе", "новая"]
    status = input("Введите текущий статус заметки: (выполнено, в процессе, новая)")
    while status not in possible_statuses:
        print('Статус введен неправильно.Введите корректный статус')
        status = input("Введите текущий статус заметки: (выполнено, в процессе, новая)")

    created_date = input('Введите дату создания заметки в формате (дд.мм.гггг):')
    while True:
        try:
            created_date = dt.strptime(created_date,'%d.%m.%Y').date()
            break
        except ValueError:
            print(f'Ошибка!!! Дату нужно ввести в формате: дд.мм.гггг (Например: 26.12.2000)')
        created_date = input('Введите дату создания заметки в формате (дд.мм.гггг):')

    issue_date = input('Введите дату истечения заметки (дедлайн) в формате (дд.мм.гггг):')
    while True:
        try:
            issue_date = dt.strptime(issue_date,'%d.%m.%Y').date()
            break
        except ValueError:
            print(f'Дэдлайн нужно ввести в формате: дд.мм.гггг (Например: 26.12.2000)')
        issue_date = input('Введите дату дедлайна в формате (дд.мм.гггг):')
    #Собираем данные заметки в словарь
    note = {'Имя пользователя': username,
        'Заголовок': unique,
        'Содержание': content,
        'Статус': status,
        'Дата создания заметки': created_date.strftime('%d.%m.%Y'),
        'Дата истечения заметки': issue_date.strftime('%d.%m.%Y')}
    return note

def main():
    note_list = []
    while True:
        note1 = create_note()
        note_list.append(note1)
        new_note = input('Хотите добавить еще одну заметку? (да/нет)')
        if new_note == 'да' or new_note == 'Да':
            continue
        if new_note == 'Нет' or new_note == 'нет':
            for id_note, note1 in enumerate(note_list,1):
                print('Список заметок:')
                print(f'{id_note}. Имя пользователя: {note1['Имя пользователя']}')
                print(f'Заголовок заметки: {note1['Заголовок']}')
                print(f'Описание заметки: {note1['Содержание']}')
                print(f'Статус заметки: {note1['Статус']}')
                print(f'Дата создания заметки: {note1['Дата создания заметки']}')
                print(f'Дата истечения заметки: {note1['Дата истечения заметки']}')
                list(note_list)
            break
        else:
            print('Некорректный ввод. "Менеджер заметок" завершил свою работу')
            for id_note in enumerate(note_list, 1):
                print(f'Список заметок:\n{id_note}. Имя пользователя: {note1['Имя пользователя']}')
                print(f'Заголовок заметки: {note1['Заголовок']}')
                print(f'Описание заметки: {note1['Содержание']}')
                print(f'Статус заметки: {note1['Статус']}')
                print(f'Дата создания заметки: {note1['Дата создания заметки']}')
                print(f'Дата истечения заметки: {note1['Дата истечения заметки']}')
                list(note_list)
            break


main()




