import datetime

def get_employees():
    print(f"--- Функция get_employees ---")
    print(f"Текущая дата: {datetime.date.today().strftime('%d/%m/%Y')}")
    print("Список сотрудников получен.")
    print("-----------------------------")