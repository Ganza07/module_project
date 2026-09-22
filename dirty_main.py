# dirty_main.py
from application.salary import *  # Импортируем всё из модуля
from application.db.people import *

import datetime

if __name__ == '__main__':
    print("Это 'грязный' импорт.\n")
    calculate_salary()
    get_employees()