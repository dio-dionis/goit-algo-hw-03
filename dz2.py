import random

def get_numbers_ticket(min, max, quantity):
    # Перевіряємо коректність вхідних даних
    if not (1 <= min < max <= 1000):
        return []
    if not (1 <= quantity <= (max - min + 1)):
        return []
    
    # Генеруємо унікальні випадкові числа
    numbers = random.sample(range(min, max + 1), quantity)
    
    # Повертаємо відсортований список
    return sorted(numbers)


# Приклади використання:
print(get_numbers_ticket(1, 49, 6))    # Наприклад: [4, 15, 23, 28, 37, 45]
print(get_numbers_ticket(1, 36, 5))    # Наприклад: [3, 7, 15, 27, 35]
print(get_numbers_ticket(10, 20, 15))  # Помилка: кількість > діапазону → []

