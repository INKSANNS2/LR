text = input("Введите произвольный текст: ")
cleaned_text = ""
for space in text:
    if space.isalpha() or space == " ":
        cleaned_text += space.lower()
    else:
        cleaned_text += " "
words = set(cleaned_text.split())
print(f"\nУникальные слова: {len(words)}")
print(f"Все уникальные слова: {words}")
long_words = set()
for word in words:
    if len(word) > 5:
        long_words.add(word)
print(f"Длинные слова: {long_words}")
has_python = "python" in words
has_programming = "programming" in words
print(f"Найдено 'python': {has_python}")
print(f"Найдено 'programming': {has_programming}")
print(f"Найдены ключевые слова: {has_python or has_programming}")