import math
expression = input("Введите выражение (число знак число): ")
parts = expression.split()
if len(parts) != 3:
    print("Ошибка: нужно ввести число, знак и число через пробел!")
else:
    try:
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
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Ошибка: деление на ноль!"
        elif operator == '%':
            if num2 != 0:
                result = num1 % num2
            else:
                result = "Ошибка: деление на ноль!"
        elif operator == '//':
            if num2 != 0:
                result = num1 // num2
            else:
                result = "Ошибка: деление на ноль!"
        elif operator == '**':
            result = num1 ** num2
        elif operator == '%%':
            result = (num2 / 100) * num1
        elif operator == '/**':
            if num1 >= 0:
                result = math.sqrt(num1)
            else:
                result = "Ошибка: корень из отрицательного числа!"
        else:
            result = "Ошибка: неизвестная операция!"
        print("Результат: ", result )
    except ValueError:
        print("Ошибка: введите числа корректно")