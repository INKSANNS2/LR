class Task:
    """Класс для представления задачи."""
    
    def __init__(self, description: str, priority: int):
        """
        Инициализация задачи.
        
        Args:
            description: Описание задачи
            priority: Приоритет задачи (целое число)
        """
        self.description = description
        self.priority = priority

class TaskManager:
    """Класс для управления задачами."""
    
    def __init__(self):
        """Инициализация менеджера задач с пустым списком."""
        self.tasks = []
    
    def add_task(self, description: str, priority: int) -> None:
        """
        Добавляет новую задачу в список.
        
        Args:
            description: Описание задачи
            priority: Приоритет задачи
        """
        new_task = Task(description, priority)
        self.tasks.append(new_task)
    
    def show_tasks(self) -> None:
        """Выводит все задачи в формате 'Описание - Приоритет'."""
        for task in self.tasks:
            print(f"{task.description} - {task.priority}")
               
    def get_high_priority_tasks(self, min_priority: int) -> list:
        """
        Возвращает список задач с высоким приоритетом.
        
        Args:
            min_priority: Минимальный приоритет для отбора задач
        
        Returns:
            Список задач с приоритетом >= min_priority
        """
        return [task for task in self.tasks if task.priority >= min_priority]

manager = TaskManager()
manager.add_task("Купить хлеб", 1)
manager.add_task("Сделать домашку", 10)
manager.add_task("Почитать книгу", 3)
manager.add_task("Подготовить проект", 8)

print("Все задачи:")
manager.show_tasks()

print("\nВажные задачи (приоритет 5+):")
important = manager.get_high_priority_tasks(5)
for task in important:
    print(task.description)