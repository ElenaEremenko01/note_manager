from datetime import datetime as dt

username = input('Введите имя пользователя:').strip()
title_list = []
for i in range(3):
    title = input('Введите заголовок заметки:').strip()
    title_list.append(title)

content = input('Опишите заметку:' ).strip()
status = input('Укажите статус заметки:' ).strip()
while True:
    created_date = input('Введите дату создания заметки в формате (дд.мм.гггг):').strip()
    try:
        created_date = dt.strptime(created_date, '%d.%m.%Y').date()
        break
    except ValueError:
        print('Дата может быть в формате(дд.мм.гггг). Например: 02.01.2000')

while True:
    issue_date = input('Введите дату истечения заметки (дедлайн) в формате (дд.мм.гггг):').strip()
    try:
        issue_date = dt.strptime(issue_date, '%d.%m.%Y').date()
        break
    except ValueError:
        print('Дата может быть в формате(дд.мм.гггг). Например: 02.01.2000')

note = [{'Имя пользователя':username,
         'Содержание заметки':content,
         'Статус':status,
         'Дата создания':created_date,
         'Дата дэдлайна': issue_date,
         'Заголовок': title_list}]

print(f'Имя пользователя: {note[0]['Имя пользователя']}')
print(f'Содержание заметки: {note[0]['Содержание заметки']}')
print(f'Статус заметки: {note[0]['Статус']}')
print(f'Дата создания заметки: {note[0]['Дата создания']}')
print(f'Дата дэдлайна заметки: {note[0]['Дата дэдлайна']}')
print(f'Заголовок: {note[0]['Заголовок']}')
