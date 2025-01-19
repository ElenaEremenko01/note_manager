
import json
# функция сохраняет заметки в формате JSON
# каждая заметка записывается в виде словаря
# весь список заметок сохраняется как JSON-структура
# возвращает файл с сериализованными заметками
def save_notes_to_file(notes, filename):
    try:
        # если файл будет не найден, то создадим новый файл
        with open('new_file_json.txt', 'x', encoding='utf-8') as file:
            # записываем данные в файл в json для сериализации с отступами
            json.dump(notes, file, indent=4, ensure_ascii=False)
            j_file = json.dumps(notes, indent=4, ensure_ascii=False)
            print(j_file)
        return file

    except FileExistsError:
    # открываем текстовый файл в режиме записи, если он существует
        with open(filename, 'w', encoding='utf-8') as file:
            # записываем данные в файл в json для сериализации с отступами
            json.dump(notes, file, indent=4, ensure_ascii=False)
            j_file = json.dumps(notes, indent=4, ensure_ascii=False)
            print(j_file)
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
    save_notes_to_file(test_note, 'data.txt')