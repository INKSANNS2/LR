stats = {}
print("Введите текст:")
while True:
    line = input()
    if line == "":
        break
    remove = "!?,.;:()[]{}'\""
    clean = line
    for sign in remove:
        clean = clean.replace(sign, " ")
    words = clean.lower().split()
    for word in words:
        if word in stats:
            stats[word] += 1
        else:
            stats[word] = 1
print("Статистика слов:")
print(stats)