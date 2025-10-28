txt = input("Введите строку: ")
lett = "аеёиоуыэюяaeiouy"
lett += lett.upper()
res = ""
index = 0
while index < len(txt):
    char = txt[index]
    if char not in lett:
        res += char
    index += 1
print("Результат:", res)