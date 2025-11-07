book = {
    "Ангелина": "89161234567",
    "Даниил": "89169876543",
    "Афанасий": "89165554433"
}
while True:
    print("\nТелефонная книга")
    print("1 - Показать все контакты")
    print("2 - Добавить контакт")
    print("3 - Удалить контакт")
    print("4 - Выйти") 
    choice = input("Выберите действие: ") 
    if choice == "1":
        print("\nВсе контакты:")
        if book:
            for name, phone in book.items():
                print(f"{name}: {phone}")
        else:
            print("Телефонная книга пуста") 
    elif choice == "2":
        name = input("Введите имя контакта: ")
        if name in book:
            print("Контакт существует")
        else:
            phone = input("Введите номер телефона: ")
            book[name] = phone
            print(f"Контакт {name} добавлен")   
    elif choice == "3":
        name = input("Введите имя контакта для удаления: ")
        if name in book:
            del book[name]
            print(f"Контакт {name} удален")
        else:
            print("Контакт не найден")
    elif choice == "4":
        print("Пока")
        exit()
    else:
        print("Неверный выбор")