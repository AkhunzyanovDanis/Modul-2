from task_1 import Smartphone, Automobile, Table

if __name__ == "__main__":
    # Создаем объекты
    phone = Smartphone("Samsung", "Galaxy S23", 128)
    car = Automobile("Tesla Model 3", "red", 250)
    table = Table(75, 120)

    # Тестируем с неправильными данными
    tests = [
        (phone.set_memory, -64, "объем памяти"),
        (car.change_speed, -30, "скорость"),
        (table.increase_length, -20, "длина стола")
    ]

    for method, value, param_name in tests:
        try:
            method(value)
        except ValueError:
            print(f"Ошибка: Некорректное значение для {param_name} ({value})")