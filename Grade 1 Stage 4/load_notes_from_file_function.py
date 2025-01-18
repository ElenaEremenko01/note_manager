
#Создаем функцию для чтения заметок из файла
#Параметры функции - текстовый документ
#Функция возвращает словари с заметками, вложенными в список
def load_notes_from_file(filename):
    # Открываем файл в режиме чтения с кодировкой для чтения кириллицы
    with open(filename, 'r', encoding='utf-8') as file:
        # Разделяем заметку на строки
        lines = file.readlines()
        #Создаем пустой список и словарь
        notes = []
        note = {}
        # В цикле проходимся по всем строкам и убираем пробелы и разделители
        for line in lines:
            line = line.strip()
            # Если строка начинается на разделение, добавляем ее в словарь и затем в список
            if line == '_' * 30 :
                if note:
                    notes.append(note)
                    # возвращаем пустой словарь для новой заметки
                    note = {}
            # разделяем заметку на ключ: значение
            if ': ' in line:
                key, value = line.split(': ', 1)
                note.update({key: value})
        # добавляем последнюю заметку в словарь и список
        if note:
            notes.append(note)

        # в цикле заменяем название ключей
        for note in notes:
            note['username'] = note.pop('Имя пользователя')
            note['title'] = note.pop('Заголовок')
            note['content'] = note.pop('Описание')
            note['status'] = note.pop('Статус')
            note['created_date'] = note.pop('Дата создания')
            note['issue_date'] = note.pop('Дедлайн')

    return notes





if __name__ == "__main__":
    print(load_notes_from_file('loading.txt'))
