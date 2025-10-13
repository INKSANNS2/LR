password = input("Придумайте пароль: ")
password2 = input("Подтвердите пароль: ")
if password != password2:
    print("Пароли не совпадают")
else:
    print("Пароль успешно установлен")
    password3 = input("Введите пароль для входа: ")
    if password3 == password:
        print("Access")
    else:
        print("Denied")