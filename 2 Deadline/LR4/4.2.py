num1 = [34, 67, 23, 89, 12, 56, 78, 45, 91, 33]
even = []
for num in num1:
    if num % 2 == 0:
        even.append(num)
large = []
for num in num1:
    if num > 50:
        large.append(num)
print(f"Исходный список: {num}")
print(f"Четные числа: {even}")
print(f"Числа больше 50: {large}")