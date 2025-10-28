num = int(input("Введите число: "))
count = 0
while num > 0:
    digit = num % 10
    count += digit
    num = num // 10
print("Сумма цифр:",count)