username = 'Elena'
title = 'Homework'
content = 'To create 6 covariates'
status = 'In work'
# импортируем из библиотеки datetime класс date, чтоб работать с датами
from datetime import datetime
#используем функцию now, чтоб вывести формат даты, а затем strftime, чтоб вывести дату в
#                                                                    определенном формате
created_date = datetime.now().strftime('27-12-2024')
issue_date = datetime.now().strftime('31-12-2024')

print('Имя пользователя:', username)
print('Заголовок заметки:', title)
print('Описание заметки:', content)
print('Статус заметки:', status)
print('Дата создания заметки:', created_date)
print('Дата истечения заметки (дэдлайн):', issue_date)