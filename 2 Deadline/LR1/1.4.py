from random import randint
rand_num = randint(1, 100)
while True:
    num = int(input("Введите ваше число: "))  
    if num == rand_num:
        print("Угадал")
        break
    elif num < rand_num:
        print("Больше")
    else:
        print("Меньше")