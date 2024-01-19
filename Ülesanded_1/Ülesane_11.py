from datetime import datetime

today = datetime.now().date()
birthday = input("Введите ваш день рождения в формате 'ДД-ММ-ГГГГ': ")
birthday_date = datetime.strptime(birthday, "%d-%m-%Y").date()
if today.day == birthday_date.day and today.month == birthday_date.month:
    print("С днем рождения! Сегодня ваша годовщина!")
else:
    print("Сегодня не ваша годовщина. Поздравляем вас в следующий раз!")
