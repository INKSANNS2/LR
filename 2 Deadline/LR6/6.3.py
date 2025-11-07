def power(number, exponent=2):
    result = 1
    for i in range(exponent):
        result *= number
    return result
print(power(4, 5))