from datetime import datetime as dt
from datetime import timedelta as td

# Создаем функцию для верного отображения даты, в нужном нам формате
def validation_date(date_str):
        try:
            dt.strptime(date_str,'%d.%m.%Y').date()
            return True
        except ValueError:
            print('Неверный ввод даты. Дату нужно ввести в формате: дд.мм.гггг (Например: 26.12.2000)')
            return False

# Создаем функцию для обновления содержания заметки
def update_note(note):
    while True: # запрашивает ключ для обновления не чувствительный к регистру
        choice_for_update = input('Какие данные Вы хотели обновить?(username, title, content, status, created_date, issue_date)').lower()
        if choice_for_update not in note: # Если ключа нет в словаре выйдет сообщение об ошибке и цикл повторится
            print('Введите названия корректно. Поля для обновления могут быть: username, title, content, status, created_date, issue_date')
            continue
        if choice_for_update in ['username', 'title', 'content', 'status']: # если ключ совпадает с одни из значений в условии
            item_for_update = input(f'Введите новое значение для {choice_for_update}').lower()#вводим новое значение для обновления
            confirm_for_update = input(f'Вы действительно хотите обновить значение {choice_for_update} (да\нет)').lower() # подтверждаем запрос для обновления
            if confirm_for_update == 'да': # если ответ положительный , обновляем значение
                note[choice_for_update] = item_for_update
                print('Обновления внесены')
                one_more_update = input('Желаете обновить еще одно поле?(да\нет)').lower() #Запрашиваем еще одно поле для обновления
                if one_more_update == 'да': # если ответ да, то обновляем еще одно поле
                    continue
                elif one_more_update == 'нет': # если нет, то заканчиваем цикл
                    print('Обновления внесены')
                    break
                else:
                    print('Ответ может быть да/нет. Обновление завершено')
                    break
            else:
                print('Обновления не были внесены.')
                print('Ответ может быть да/нет. Обновление завершено')
        if choice_for_update in ['created_date', 'issue_date']: # Если ключ относится к дате, то м проверяем в цикле корректность ввода
            item_for_update = input(f'Введите новое значение для {choice_for_update}').lower()
            confirm_for_update = input(f'Вы действительно хотите обновить значение {choice_for_update} (да\нет)').lower()
            if confirm_for_update == 'да':
                if not validation_date(item_for_update): # Если дата введена неправильно, то выйдет ошибка и цикл повторится
                    print('Ошибка!!!')
                    continue
                else:
                    note[choice_for_update] = item_for_update # если дата корректная, вносим изменения
                    print('Обновления внесены')
                    break


    return list(note) # возвращаем список со словарем

notes =  {'username': 'Алексей',
              'title': 'Список покупок',
              'content': 'Купить продукты на неделю',
              'status': 'новая',
              'created_date': '27-11-2024',
              'issue_date': '30-11-2024'}

print(update_note(notes))