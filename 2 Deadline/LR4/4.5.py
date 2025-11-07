print("Введите текст:")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
full = " ".join(lines)
clean = ""
for char in full:
    if ('а' <= char <= 'я') or ('А' <= char <= 'Я') or ('a' <= char <= 'z') or ('A' <= char <= 'Z') or char == ' ':
        clean += char
    else:
        clean += " "
words = clean.lower().split()
if not words:
    print("Текст не введен")
else:
    long = words[0]
    short = words[0]
    
    for word in words:
        if len(word) > len(long):
            long = word
        if len(word) < len(short):
            short = word   
    print(f"Самое длинное слово: {long}")
    print(f"Самое короткое слово: {short}")
    length = 0
    for word in words:
        length += len(word)   
    ave = length / len(words)
    print(f"Средняя длина: {round(ave, 1)}")
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    sort = []
    for word, count in count.items():
        sort.append((word, count))
    for i in range(len(sort)):
        for j in range(i + 1, len(sort)):
            if sort[j][1] > sort[i][1]:
                sort[i], sort[j] = sort[j], sort[i]
    top = sort[:5]
    print(f"Топ-5 слов: {top}")