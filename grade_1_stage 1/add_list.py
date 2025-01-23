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

print(username)
print(title_list)
print(content)
print(status)
print(created_date.strftime('%d.%m.'))
print(issue_date.strftime('%d.%m.'))
