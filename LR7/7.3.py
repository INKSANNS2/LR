text = input("Введите текст: ")
word = input("Введите слово для поиска: ")
count = 0
for i in range(len(text)):
    if text[i:i+len(word)] == word:
        count += 1
if count > 0:
    print(f"Слово '{word}' встречается {count} раз")
else:
    print(f"Слова '{word}' нет в тексте")