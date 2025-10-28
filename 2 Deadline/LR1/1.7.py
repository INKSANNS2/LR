sym = input("Символ: ")
height = int(input("Высота: "))
width = int(input("Ширина: "))
i = 0
while i < height:
    if i == 0 or i == height - 1:
        print(sym * width)
    else:
        line = sym + " " * (width - 2) + sym
        print(line)
    i += 1