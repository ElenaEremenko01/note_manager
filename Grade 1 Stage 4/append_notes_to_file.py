

# функция содержит параметры:
# notes - список заметок (список со словарями)
# filename - файл, куда будем записывать заметки
# возвращаем файл с заметками
def save_notes_to_file(notes, filename):
    try:
        # если файл будет не найден, то создадим новый файл
        with open('new_file.txt', 'x', encoding='utf-8') as file:
            # в цикле проходимся по всем заметкам в списке и записываем в файл
            for note in notes:
                file.write(f'Имя пользователя: {note["username"]}\n')
                file.write(f'Заголовок: {note["title"]}\n')
                file.write(f'Описание: {note["content"]}\n')
                file.write(f'Статус: {note["status"]}\n')
                file.write(f'Дата создания: {note["created_date"]}\n')
                file.write(f'Дедлайн: {note["issue_date"]}\n')
                file.write(f'_' * 30 + '\n')
                print(f'Файл {filename} не найден. Создан новый файл.')
    except FileExistsError:
    # открываем текстовый файл в режиме добавления к записанному
        with open(filename, 'a', encoding='utf-8') as file:
            # в цикле проходимся по всем заметкам в списке и записываем в файл
            for note in notes:
                file.write(f'Имя пользователя: {note["username"]}\n')
                file.write(f'Заголовок: {note["title"]}\n')
                file.write(f'Описание: {note["content"]}\n')
                file.write(f'Статус: {note["status"]}\n')
                file.write(f'Дата создания: {note["created_date"]}\n')
                file.write(f'Дедлайн: {note["issue_date"]}\n')
                file.write(f'_' * 30 + '\n')
            return file

if __name__ == "__main__":
    test_note = [
        {"username": "Алексей", "title": "Список покупок", "content": "Купить продукты на неделю", "status": "новая",
         "created_date": "27.11.2024", "issue_date": "30.11.2024"},
        {"username": "Мария", "title": "Учеба", "content": "Подготовиться к экзамену", "status": "в процессе",
         "created_date": "25.11.2024", "issue_date": "01.12.2024"},
        {"username": "Иван", "title": "Работа", "content": "Закончить отчёт", "status": "в процессе",
         "created_date": "20.11.2024", "issue_date": "28.11.2024"},
        {"username": "Ольга", "title": "Здоровье", "content": "Записаться к врачу", "status": "новая",
         "created_date": "18.11.2024", "issue_date": "23.11.2024"},
        {"username": "Дмитрий", "title": "Отпуск", "content": "Собрать документы", "status": "новая",
         "created_date": "15.11.2024", "issue_date": "20.11.2024"}, ]

    save_notes_to_file(test_note, 'filename.txt')



