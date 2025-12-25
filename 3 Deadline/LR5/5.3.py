class Animal:
    """Базовый класс для всех животных."""
    
    def __init__(self, name: str):
        """
        Инициализация животного.
        
        Args:
            name: Имя животного
        """
        self.name = name
    
    def make_sound(self) -> None:
        """Издает звук животного."""
        print("Животное издает звук")

class Dog(Animal):
    """Класс для собаки."""
    
    def make_sound(self) -> None:
        """Издает звук собаки."""
        print("Гав!")

class Cat(Animal):
    """Класс для кошки."""
    
    def make_sound(self) -> None:
        """Издает звук кошки."""
        print("Мяу!")

def animal_chorus(animals: list) -> None:
    """
    Вызывает метод make_sound() у каждого животного в списке.
    
    Args:
        animals: Список объектов животных
    """
    for animal in animals:
        animal.make_sound()

animals = [Dog("Sharik"), Cat("Matroskin")]
animal_chorus(animals)