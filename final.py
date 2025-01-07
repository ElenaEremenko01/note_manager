username = input('Введите имя пользователя:' )
title1 = input('Введите заголовок заметки:')
title2 = input('Введите заголовок заметки:')
title3 = input('Введите заголовок заметки:')
title_list = [title1 , title2, title3]
content = input('Опишите заметку:' )
status = input('Укажите статус заметки:')
created_date = input('Введите дату создания заметки в формате (дд.мм.):')
issue_date = input('Введите дату истечения заметки (дедлайн) в формате (дд.мм.):')

note_dict = {'Имя пользователя': username,
        'Содержание заметки': content,
         'Статус': status,
        'Дата создания': created_date,
        'Дата изменения': issue_date,
        'Заголовок':title_list}
note = [note_dict['Имя пользователя'],
        note_dict['Содержание заметки'],
        note_dict['Статус'],
        note_dict['Дата создания'],
        note_dict['Дата изменения'], note_dict['Заголовок']]
print(note)



