# Импортируем функции
from application.salary import calculate_salary
from application.db.people import get_employees

import datetime

if __name__ == '__main__':
    print(f"Запуск программы. Дата: {datetime.date.today().strftime('%d/%m/%Y')}\n")

    # Вызываем функции
    calculate_salary()
    get_employees()
