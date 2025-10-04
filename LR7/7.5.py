import math
text = input("Введите числа и операцию через пробел: ")
parts = text.split()

if parts[1] == '/**':
    num = float(parts[0])
    result = math.sqrt(num)
else:
    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    elif operator == '%':
        result = num1 % num2
    elif operator == '//':
        result = num1 // num2
    elif operator == '**':
        result = num1 ** num2
    elif operator == '%%':
        result = num1 * num2 / 100
    else:
        result = "неизвестная операция"
print("Ответ:", result)
