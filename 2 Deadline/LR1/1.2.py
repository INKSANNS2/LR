count = 0
num = 1
while num != 0:
    num = int(input("Введите число: "))
    if num != 0:
        count += 1
print("Количество чисел до первого нуля:", count)