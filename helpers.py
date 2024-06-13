import random

from locators.order_page_locators import OrderPagesLocators


def generate_phone_number():
    return random.randint(10000000000, 99999999999)


def generate_user_data():
    user_data = {
        'name': random.choices(['Маша', 'Саша', 'Паша', 'Даша']),
        'last_name': random.choices(['Сидоренко', 'Голубь', 'Грац', 'Петренко']),
        'address': random.choices(['Каляева, 13', 'Пушкина, 462', 'Мира, 174']),
        'phone_number': generate_phone_number()
    }
    return user_data


def generate_order_data():
    order_data = {
        'date': f'{random.randint(1, 28)}.{random.randint(1, 12)}.2024',
        'color': random.choice([OrderPagesLocators.CHECKBOX_BLACK, OrderPagesLocators.CHECKBOX_GREY]),
        'comment': 'Я буду в синей майке'
    }
    return order_data


def generate_number_metro_station():
    num = random.randint(0, 224)
    return num
