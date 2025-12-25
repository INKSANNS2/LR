class Student:
    """Класс для представления студента."""
    
    def __init__(self, name: str, average_score: float):
        """
        Инициализация студента.
        
        Args:
            name: Имя студента
            average_score: Средний балл студента
        """
        self.name = name
        self.average_score = average_score
    
    def is_excellent(self) -> bool:
        """
        Проверяет, является ли студент отличником.
        
        Returns:
            True если средний балл равен 5, иначе False
        """
        return self.average_score == 5
# Пример использования
student1 = Student("Vasya", 5)
student2 = Student("Petya", 1.67)
print(student1.is_excellent())  
print(student2.is_excellent())  