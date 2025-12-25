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


manager = TaskManager()
manager.add_task("Купить хлеб", 1)
manager.add_task("Сделать домашку", 10)
manager.show_tasks()