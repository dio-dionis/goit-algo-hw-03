from datetime import datetime

def get_days_from_today(date):
    try:
        # Перетворюємо рядок у дату
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
        
        # Отримуємо поточну дату
        today = datetime.today().date()
        
        # Різниця у днях (може бути від’ємна)
        delta = today - target_date
        
        # Повертаємо кількість днів як ціле число
        return delta.days
    
    except ValueError:
        # Якщо формат дати неправильний
        print("Помилка: дата повинна бути у форматі 'РРРР-ММ-ДД'")
        return None


# Приклади використання:
print(get_days_from_today("2021-10-09"))  # приклад із завдання
print(get_days_from_today("2025-10-01"))  # приклад з майбутньою датою
print(get_days_from_today("2020/10/09"))  # приклад з помилковим форматом
