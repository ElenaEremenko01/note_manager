from datetime import datetime as dt

while True:
    created_date = input('Введите дату создания заметки в формате (дд.мм.гггг):')
    try:
        created_date = dt.strptime(created_date,'%d.%m.%Y').date()
        print(created_date.strftime('%d.%m.'))
        break
    except ValueError:
        print('Дата может быть в формате(дд.мм.гггг). Например: 02.01.2000')

while True:
    issue_date = input('Введите дату истечения заметки (дедлайн) в формате (дд.мм.гггг):')
    try:
        issue_date = dt.strptime(issue_date,'%d.%m.%Y').date()
        print(issue_date.strftime('%d.%m.'))
        break
    except ValueError:
        print('Дата может быть в формате(дд.мм.гггг). Например: 02.01.2000')







