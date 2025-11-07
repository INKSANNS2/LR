text = input("Введите произвольную строку: ").lower()
count = {}
for char in text:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

# 4. Выводим результат
print("Результат подсчета символов:")
print(count)