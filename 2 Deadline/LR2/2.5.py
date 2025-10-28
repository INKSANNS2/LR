n = int(input("Сколько чисел вы хотите ввести? "))
numbers = []
total = 0
for i in range(n):
    num = float(input(f"Введите число {i + 1}: "))
    numbers.append(num)
    total += num
max = max(numbers)
min = min(numbers)
average = total / n
count_above_average = 0
for num in numbers:
    if num > average:
        count_above_average += 1
print("\nРезультаты:")
print(f"Максимальное: {max}")
print(f"Минимальное: {min}")
print(f"Среднее: {average}")
print(f"Чисел больше среднего: {count_above_average}")