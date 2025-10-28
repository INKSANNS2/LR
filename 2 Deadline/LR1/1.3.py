text = input("Введите строку: ")
clean_txt = text.lower().replace(" ", "")
left = 0
right = len(clean_txt) - 1
palin = True
while left < right:
    if clean_txt[left] != clean_txt[right]:
        palin = False
        break
    left += 1
    right -= 1
if palin:
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")