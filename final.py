username = input('Введите имя пользователя:' )
title = input('Введите заголовок заметки:' )
subtitle1 = input('Введите подзаголовок №1:')
subtitle2 = input('Введите подзаголовок №2:')
subtitle3 = input('Введите подзаголовок №3:')
subtitle = [subtitle1 , subtitle2, subtitle3]
content = input('Опишите заметку:' )
status = input('Укажите статус заметки:' )
created_date = input('Введите дату создания заметки в формате (дд.мм.):')
issue_date = input('Введите дату истечения заметки (дедлайн) в формате (дд.мм.):')

note = {'Имя пользователя':username, 'Заголовок': [title, subtitle], 'Содержание':content, 'Статус':status,
    'Дата создания заметки':created_date[0:5], 'Дата истечения заметки':issue_date[0:5]}

print(note)
