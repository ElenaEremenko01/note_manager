
note_try = [{'Имя': 'Алексей', 'Заголовок': 'Купить продукты на неделю', 'Описание': 'Купить продукт на неделю'},
         {'Имя': 'Мария', 'Заголовок': 'Учеба', 'Описание': 'Подготовиться к экзамену'},
         {'Имя': 'Елена', 'Заголовок': 'Книга', 'Описание': 'Написать книгу'}]
# создаем функцию для отображения списка заметок
def display_notes(notes):
    if not notes:
        print('Список заметок пуст')
    else:
        print('Текущий список заметок:')
        for i in range(len(notes)):
            print(f'{i+1}. Имя: {notes[i]['Имя']}')
            print(f'Заголовок: {notes[i]['Заголовок']}')
            print(f'Описание: {notes[i]['Описание']}')

display_notes(note_try)
# запускаем цикл, с запросом удаления заметки
while True:
    deletion = input('Желаете удалить заметку?(да\нет)').lower()
    if deletion == 'да': # Если заметку хотят удалить запускаем цикл для проверки введенных параметров
        note_del = input('Введите имя пользователя или заголовок для удаления заметки:').lower()
        for i in reversed(range(len(note_try))):
            if note_try[i]['Имя'].lower() == note_del:
                confirmation2 = input('Вы уверены, что хотите удалить заметку?(да\нет)').lower()
                if confirmation2 == 'да':
                    del note_try[i]
                    print('Заметка успешно удалена')
                    display_notes(note_try)
                    break
            elif note_try[i]['Заголовок'].lower() == note_del:
                confirmation3 = input('Вы уверены, что хотите удалить заметку?(да\нет)').lower()
                if confirmation3 == 'да':
                    del note_try[i]
                print('Заметка успешно удалена')
                display_notes(note_try)
                break
            else:
                print('Заметки с такими параметрами нет')
                display_notes(note_try)
    elif deletion == 'нет': # Если заметку не хотят удалять программа завершиться
        display_notes(note_try)
        break
    elif not note_try: # Если заметок не останется на экране отобразиться следующий ответ
        print('Список заметок пуст')
        break
    else: # Если ввод будет неверным цикл повториться и отобразится подсказка
        print('Ошибка неверный ввод. Ответ может быть: "да" или "нет"')
        display_notes(note_try)



