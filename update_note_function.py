from datetime import datetime as dt
from datetime import timedelta as td
from tabulate import tabulate
from colorama import Fore, Style, init
init(autoreset= True)

# Создаем функцию для обновления содержания заметки
def update_note(note):
    while True: # запрашивает ключ для обновления не чувствительный к регистру
        choice_for_update = input(f'Какие данные Вы хотели обновить?{Fore.YELLOW}(username, title, content, status, created_date, issue_date)').strip().lower()
        if choice_for_update not in note: # Если ключа нет в словаре выйдет сообщение об ошибке и цикл повторится
            print(f'{Fore.RED}Введите названия корректно. {Fore.RESET}Поля для обновления могут быть:{Fore.YELLOW}{Style.BRIGHT} username, title, content, status, created_date, issue_date')
            continue
        if choice_for_update in ['username', 'title', 'content', 'status']: # если ключ совпадает с одним из значений в условии
            item_for_update = input(f'Введите новое значение для {choice_for_update}').strip().lower()#вводим новое значение для обновления
            confirm_for_update = input(f'Вы действительно хотите обновить значение {choice_for_update} {Fore.YELLOW}{Style.BRIGHT}(да\нет)').strip().lower() # подтверждаем запрос для обновления
            if confirm_for_update == 'да': # если ответ положительный, обновляем значение
                note[choice_for_update] = item_for_update
                print(f'{Fore.GREEN}Обновления внесены')
                one_more_update = input(f'Желаете обновить еще одно поле?{Fore.YELLOW}{Style.BRIGHT}(да\нет)').lower() #Запрашиваем еще одно поле для обновления
                if one_more_update == 'да': # если ответ да, то обновляем еще одно поле
                    continue
                elif one_more_update == 'нет': # если нет, то заканчиваем цикл
                    print(f'{Fore.GREEN}Обновления внесены')
                    break
                else:
                    print(f'Ответ может быть {Fore.YELLOW}{Style.BRIGHT}да/нет. {Fore.RESET}{Style.NORMAL}Обновление завершено')
                    break
            elif confirm_for_update == 'нет':
                print(f'{Style.BRIGHT}Обновления не были внесены.')
                continue

            else:
                print(f'{Style.BRIGHT}Обновления не были внесены.')
                print(f'Ответ может быть {Fore.YELLOW}{Style.BRIGHT}да/нет {Fore.RESET}{Style.NORMAL}Обновление завершено')
        if choice_for_update in ['created_date', 'issue_date']: # Если ключ относится к дате, то м проверяем в цикле корректность ввода
            item_for_update = input(f'Введите новое значение для {choice_for_update}').strip().lower()
            try:
                item_for_update = dt.strptime(item_for_update, '%d.%m.%Y').date()
            except ValueError:
                print(f'{Fore.RED}Ошибка!!!')
                print(f'Дату можно ввести в формате дд.мм.гггг (Например: 01.01.2000)')
                continue
            confirm_for_update = input(f'Вы действительно хотите обновить значение {choice_for_update} {Fore.YELLOW}{Style.BRIGHT}(да\нет)').strip().lower()
            if confirm_for_update == 'да':
                note[choice_for_update] = dt.strftime(item_for_update,'%d.%m.%Y')
                print(f'{Fore.GREEN}Обновления внесены')
                one_more_update = input(f'Желаете обновить еще одно поле?{Fore.YELLOW}{Style.BRIGHT}(да\нет)').lower()
                if one_more_update == 'да':
                    continue
                elif one_more_update == 'нет':
                    print(f'{Fore.GREEN}Обновления внесены')
                    break
                else:
                    print(f'Ответ может быть {Fore.YELLOW}{Style.BRIGHT}да/нет. {Fore.RESET}{Style.NORMAL}Обновление завершено')
                    break
            elif confirm_for_update == 'нет':
                print(f'{Style.BRIGHT}Обновления не были внесены.')
                continue
            else:
                print(f'{Style.BRIGHT}Обновления не были внесены.')
                print(f'Ответ может быть {Fore.YELLOW}{Style.BRIGHT}да/нет {Fore.RESET}{Style.NORMAL}Обновление завершено')


    return list(note) # возвращаем список со словарем

notes =  {'username': 'Алексей',
              'title': 'Список покупок',
              'content': 'Купить продукты на неделю',
              'status': 'новая',
              'created_date': '27-11-2024',
              'issue_date': '30-11-2024'}

if __name__ == "__main__":
    new_note = update_note(notes)
