task = []
while True:
    print("\nМеню задач")
    print("1 - Показать все задачи")
    print("2 - Добавить задачу")
    print("3 - Отметить задачу как выполненную")
    print("4 - Выйти")  
    choice = input("Выберите действие: ")    
    if choice == "1":
        if not task:
            print("Задач нет")
        else:
            print("Ваши задачи:")
            for i, task in enumerate(task, 1):
                print(f"{i}. {task}")    
    elif choice == "2":
        new= input("Введите описание задачи: ")
        task.append(new)
        print(f"Задача '{new}' добавлена")
    elif choice == "3":
        if not task:
            print("Задач нет")
        else:
            print("Ваши задачи:")
            for i, task in enumerate(task, 1):
                print(f"{i}. {task}")            
            try:
                num = int(input("Какую задачу выполнили? ")) - 1
                if 0 <= num < len(task):
                    remove = task.pop(num)
                    print(f"Задача '{remove}' удалена")
                else:
                    print("Неверный номер задачи")
            except ValueError:
                print("Введите число")    
    elif choice == "4":
        print("Пока")
        break
    else:
        print("Неверный выбор")