
note_try = [{'Имя': 'Алексей', 'Заголовок': 'Купить продукты на неделю', 'Описание': 'Купить продукт на неделю'},
         {'Имя': 'Мария', 'Заголовок': 'Учеба', 'Описание': 'Подготовиться к экзамену'},
         {'Имя': 'Елена', 'Заголовок': 'Книга', 'Описание': 'Написать книгу'}]

print('Текущий список заметок:')
for i in range(len(note_try)):
    print(f'{i+1}. Имя: {note_try[i]['Имя']}')
    print(f'Заголовок: {note_try[i]['Заголовок']}')
    print(f'Описание: {note_try[i]['Описание']}')
deletion = input('Желаете удалить заметку?(да\нет)').lower()
while True:
    if deletion == 'да':
        note_del = input('Введите имя пользователя или заголовок для удаления заметки:').lower()
        for i in reversed(range(len(note_try))):
            if note_try[i]['Имя'].lower() == note_del:
                confirmation2 = input('Вы уверены, что хотите удалить заметку?(да\нет)').lower()
                if confirmation2 == 'да':
                    del note_try[i]
                    print('Заметка успешно удалена')
                    for j in reversed(range(len(note_try))):
                        print('Текущий список заметок:')
                        print(f'{j + 1}. Имя: {note_try[j]['Имя']}')
                        print(f'Заголовок: {note_try[j]['Заголовок']}')
                        print(f'Описание: {note_try[j]['Описание']}')
                        break
            elif note_try[i]['Заголовок'].lower() == note_del:
                confirmation3 = input('Вы уверены, что хотите удалить заметку?(да\нет)').lower()
                if confirmation3 == 'да':
                    del note_try[i]
                print('Заметка успешно удалена')
                for j in reversed(range(len(note_try))):
                    print('Текущий список заметок:')
                    print(f'{j + 1}. Имя: {note_try[j]['Имя']}')
                    print(f'Заголовок: {note_try[j]['Заголовок']}')
                    print(f'Описание: {note_try[j]['Описание']}')
                    break
            elif note_try[i]['Имя'].lower() != note_del:
                print('Заметки с данным именем нет')
                break
            elif note_try[i]['Заголовок'].lower() != note_del:
                print('Заметки с данным заголовком нет')
                break
            elif i not in note_try:
                print('Список заметок пуст')
                break
    elif not note_try:
            print('Список заметок пуст')
            break
    elif deletion == 'нет':
        print('Текущий список заметок:')
        for i in range(len(note_try)):
            print(f'{i + 1}. Имя: {note_try[i]['Имя']}')
            print(f'Заголовок: {note_try[i]['Заголовок']}')
            print(f'Описание: {note_try[i]['Описание']}')
        break
    else:
        print('Ошибка неверный ввод. Ответ может быть: "да" или "нет"')
        print('Текущий список заметок:')
        for i in range(len(note_try)):
            print(f'{i + 1}. Имя: {note_try[i]['Имя']}')
            print(f'Заголовок: {note_try[i]['Заголовок']}')
            print(f'Описание: {note_try[i]['Описание']}')
        deletion = input('Желаете удалить заметку?(да\нет)').lower()


