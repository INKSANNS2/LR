def sum_numbers(*args: float) -> float:
    """
    Возвращает сумму произвольного количества числовых аргументов.   
    Args:
        *args: Произвольное количество числовых аргументов      
    Returns:
        float: Сумма всех переданных чисел
    """
    total = 0.0
    for num in args:
        total += num
    return total
print(sum_numbers(1, 2, 3, 4, 5))