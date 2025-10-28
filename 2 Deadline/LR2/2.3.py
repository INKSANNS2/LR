txt = input("Введите текст: ")
l_count = 0
d_count = 0
p_count = 0
s_count = 0
p = ".,!?:;"
l = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
d = "1234567890"
s = " "
for i in txt:
    if i in l:
        l_count += 1
    elif i in d:
        d_count += 1
    elif i in p:
        p_count += 1
    elif i in s:
        s_count += 1
print(f"букв = {l_count}")
print(f"цифр = {d_count}")
print(f"знаков препинания = {p_count}")
print(f"пробелов = {s_count}")