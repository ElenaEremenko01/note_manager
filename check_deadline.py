# импортируем класс datetime из библиотеки datetime, как dt(для удобства и сокращения кода)
from datetime import datetime as dt
# импортируем класс datetime из библиотеки datetime, как dt(для удобства и сокращения кода)
from datetime import date
# вводим переменную
issue_date = input('Введите дату истечения заметки (дедлайн) в формате (дд.мм.гггг):')
# вводим дополнительную переменную для работы в цикле, которая выводит текущую дату без времени
now = dt.now().date()
# Используем цикл для вывода ошибки
while True:
    try: # если пользователь введет нужный формат даты, то цикл остановится
        issue_date = dt.strptime(issue_date,'%d.%m.%Y').date()# преобразуем дату в нужный формат день- 2 цифры, месяц- 2 цифры и год- 4 цифры
        print('Дата дэдлайна:', issue_date.strftime('%d.%m.%Y'))
        break
    except ValueError: # при неверном воде выйдет ошибка ValueError, мы вместо нее введем нужное сообщение
        print(f'Дэдлайн нужно ввести в формате: дд.мм.гггг (Например: 26.12.2000)')
    issue_date = input('Введите дату дедлайна в формате (дд.мм.гггг):')
# вводим условия для проверки даты
if now > issue_date:
    passed = now - issue_date
    print(f'Внимание!!! Дэдлайн истек {passed.days} дня назад')
elif now < issue_date:
    deadline = issue_date - now
    print(f'Дэдлайн через {deadline.days} дней')
elif now == now:
    print(f'Дэдлайн сегодня')

