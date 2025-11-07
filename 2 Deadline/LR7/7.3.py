def calc_avg(numbers: list) -> float:
    """
    Вычисляет среднее арифметическое значение списка чисел.
    Args:
        numbers: Список чисел для вычисления среднего     
    Returns:
        float: Среднее арифметическое значение
    """
    if not numbers:
        return 0.0      
    return sum(numbers) / len(numbers)
def fmt_fio(parts: list, capitalize: bool = True) -> str:
    """
    Форматирует ФИО из списка частей. 
    Args:
        parts: Список строк, представляющих части ФИО
        capitalize: Флаг для приведения к заглавным буквам   
    Returns:
        str: Отформатированная строка ФИО
    """
    fio = " ".join(parts)
    if capitalize:
        return fio.title()
    return fio
def filter_scores(data_dict: dict, min_value: int) -> dict:
    """
    Фильтрует словарь оценок по минимальному значению.
    Args:
        data_dict: Словарь с оценками
        min_value: Минимальное значение оценки   
    Returns:
        dict: Отфильтрованный словарь
    """
    result = {}
    for key, value in data_dict.items():
        if value >= min_value:
            result[key] = value       
    return result
print(calc_avg([10, 20, 30, 40]))
print(fmt_fio(["петров", "иван", "сергеевич"]))
print(fmt_fio(["сидорова", "анна", "валерьевна"], capitalize=False))
scores = {"math": 95, "history": 78, "english": 88, "art": 92}
print(filter_scores(scores, 90))