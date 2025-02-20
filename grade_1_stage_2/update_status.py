# Проверка и обновление статуса заметки из предложенных
#Программа отображает текущий статус заметки.
#Обеспечивается возможность изменить статус на один из предложенных вариантов.
#Программа корректно обрабатывает некорректный ввод


# Возможные статусы заметки
possible_statuses = ["выполнено", "в процессе", "отложено"]

# Запрос текущего статуса, который пользователь прописывает сам
current_status = input("Введите текущий статус заметки:")
print(f'\nТекущий статус заметки: "{current_status}"')
#Запускаем цикл
while True:
    # Отображение доступных вариантов статусов и запрос у пользователя
    print("Выберите новый статус заметки:\n1.выполнено\n2.в процессе\n3.отложено")
    choice = input("Ваш выбор: ").lower()
    # Запрос нового статуса используем try except, чтобы дать пользователю возможность вводить и цифровые и буквенные значения статусов
    try:
        choice1 = int(choice) # если пользователь введет число, то переменная choice преобразуется в число
        if 1 <= choice1 <= len(possible_statuses): # создаем условие, что если введенная цифра, в диапазоне от 1 до 3 (проходимся по длине списка)
        # Обновление статуса
            current_status = possible_statuses[choice1 - 1]# Текущий статус будет отображаться по индексу списка - 1 элемент (т.к. индекс начинается в 0)
            print(f'\nСтатус заметки успешно обновлён на: "{current_status}"')# выводим сообщение с измененным статусом
            break
        else: # Если пользователь введет число отличное от 1,2,3, появится сообщение ниже
            print("\nОшибка: выберите число из предложенного диапазона.")
    except ValueError: # если пользователь введет буквенное значение, то вместо ошибки ValueError, будет отработано условие
        if choice == 'выполнено' or choice == 'в процессе' or choice == 'отложено':# если пользователь введет верное значение (буквенное), то статс измениться
            print(f'\nСтатус заметки успешно обновлён на: "{choice}"')
            break
        else:
            print("\nОшибка!!! Статус может быть: выполнено, в процессе, отложено. Введите одно из значений")



