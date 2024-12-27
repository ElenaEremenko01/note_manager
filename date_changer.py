from datetime import datetime

created_date = datetime.now().strftime('26-12-2024')
issue_date = datetime.now().strftime('31-12-2024')

print('Дата создания заметки:', created_date[0:5])
print('Дата истечения заметки (дэдлайн):', issue_date[0:5])