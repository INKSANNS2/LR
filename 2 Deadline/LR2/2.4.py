n = int(input("Введите высоту: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i * 2):
        if j <= i:
            print(j, end="")
        else:
            print(i * 2 - j, end="")
    print()