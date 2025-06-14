import doctest
from typing import Union, List


class Smartphone:
    def __init__(self, brand: str, model: str, memory: int, os: str = "Android"):
        """
        >>> phone = Smartphone("Samsung", "Galaxy S23", 128)
        >>> phone.brand
        'Samsung'
        """
        self.brand = brand
        self.model = model
        self.memory = memory
        self.os = os
        self.installed_apps: List[str] = []

    def set_memory(self, new_memory: int) -> None:
        """Устанавливает новый объем памяти"""
        if not isinstance(new_memory, int):
            raise TypeError("Объем памяти должен быть целым числом")
        if new_memory < 1:
            raise ValueError("Объем памяти должен быть положительным")
        self.memory = new_memory

    def install_app(self, app_name: str) -> str:
        """Устанавливает приложение"""
        if app_name in self.installed_apps:
            return f"{app_name} уже установлено"
        self.installed_apps.append(app_name)
        return f"Приложение {app_name} успешно установлено"


class Automobile:
    def __init__(self, model: str, color: str, max_speed: int):
        """
        >>> car = Automobile("Tesla Model 3", "red", 250)
        >>> car.model
        'Tesla Model 3'
        """
        self.model = model
        self.color = color
        self.max_speed = max_speed
        self.current_speed = 0
        self.engine_on = False

    def change_speed(self, new_speed: int) -> None:
        """Изменяет текущую скорость"""
        if not isinstance(new_speed, (int, float)):
            raise TypeError("Скорость должна быть числом")
        if new_speed < 0:
            raise ValueError("Скорость не может быть отрицательной")
        if new_speed > self.max_speed:
            raise ValueError(f"Скорость не может превышать {self.max_speed} км/ч")
        self.current_speed = new_speed

    def toggle_engine(self) -> str:
        """Включает/выключает двигатель"""
        self.engine_on = not self.engine_on
        return f"Двигатель {'включен' if self.engine_on else 'выключен'}"


class Table:
    def __init__(self, height: int, length: int, material: str = "дерево"):
        """
        >>> table = Table(75, 120, "стекло")
        >>> table.material
        'стекло'
        """
        self.height = height
        self.length = length
        self.material = material
        self.extended = False

    def increase_length(self, extension: int) -> str:
        """Увеличивает длину стола"""
        if not isinstance(extension, (int, float)):
            raise TypeError("Длина должна быть числом")
        if extension < 0:
            raise ValueError("Длина не может быть отрицательной")
        self.length += extension
        self.extended = True
        return f"Длина стола увеличена на {extension} см"

    def reset_length(self) -> None:
        """Сбрасывает длину стола"""
        self.length -= (self.length - 120) if self.extended else 0
        self.extended = False



if __name__ == "__main__":
    doctest.testmod()



