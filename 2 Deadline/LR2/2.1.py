num = int(input("Введите число: "))
sum = 0
for i in range(1, num + 1):
    sum += i
print(f"Сумма чисел от 1 до {num}: {sum}")