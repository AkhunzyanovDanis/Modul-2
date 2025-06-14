class Vehicle:
    """Базовый класс для транспортных средств"""

    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year
        self._mileage = 0  # Защищенный атрибут

    def __str__(self) -> str:
        return f"{self.brand} {self.model} ({self.year})"

    def __repr__(self) -> str:
        return f"Vehicle('{self.brand}', '{self.model}', {self.year})"

    def add_mileage(self, km: int) -> None:
        """Добавляет пробег"""
        if km < 0:
            raise ValueError("Пробег не может быть отрицательным")
        self._mileage += km


class ElectricCar(Vehicle):
    """Класс электромобиля с расширенным функционалом"""

    def __init__(self, brand: str, model: str, year: int, battery: int):
        super().__init__(brand, model, year)
        self.battery = battery  # емкость батареи
        self.charge = 100  # текущий заряд

    def __str__(self) -> str:
        return f"{super().__str__()} | Заряд: {self.charge}%"

    def charge_battery(self, percent: int) -> None:
        """Заряжает батарею"""
        if not 0 <= percent <= 100:
            raise ValueError("Неверное значение заряда")
        self.charge = min(100, self.charge + percent)

    def add_mileage(self, km: int) -> None:
        """
        Перегрузка метода с учетом расхода заряда
        (1 км = 1% заряда для упрощения)
        """
        if km > self.charge:
            raise ValueError("Недостаточно заряда")
        super().add_mileage(km)
        self.charge -= km
