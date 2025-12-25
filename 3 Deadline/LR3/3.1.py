def power(a, n):
    if n == 0:
        return 1
    elif n > 0:
        return a * power(a, n - 1)
    else:
        return 1 / power(a, -n)

print(power(5, 4))
print(power(3, -2))