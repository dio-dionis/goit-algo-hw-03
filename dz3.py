import re

def normalize_phone(phone_number):
    # Видаляємо всі пробіли, табуляції, перенос рядка тощо
    phone = phone_number.strip()
    
    # Залишаємо тільки цифри та символ '+'
    phone = re.sub(r"[^\d+]", "", phone)
    
    # Якщо номер починається з '00', замінюємо на '+'
    if phone.startswith("00"):
        phone = "+" + phone[2:]
    
    # Якщо номер вже починається з '+', нічого не додаємо
    if phone.startswith("+"):
        # Якщо це український код без '+'
        if not phone.startswith("+38") and phone.startswith("+380") is False:
            # але таких випадків майже не буде — просто повертаємо як є
            return phone
        return phone

    #  Якщо номер починається з '380', додаємо лише '+'
    if phone.startswith("380"):
        return "+" + phone

    # Якщо номер починається з '0' або без міжнародного коду — додаємо '+38'
    if phone.startswith("0"):
        return "+38" + phone

    # Якщо нічого з вище не підходить — також додаємо '+38' на початок
    return "+38" + phone


#  Приклад використання:
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
