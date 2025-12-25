import time

# Функция бинарного поиска (O(log n))
def binary_search(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)

# Функция линейного поиска (O(n))
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Создаем отсортированный список
n = 10000000
print(f"Создание отсортированного списка от 0 до {n}...")
arr = list(range(n))
target = -1  # Худший случай - элемент не существует

print("\n=== Сравнение алгоритмов поиска ===")
print(f"Поиск числа {target} в списке из {n} элементов")

# Бинарный поиск
print("\n1. Бинарный поиск (O(log n)):")
start_time = time.time()
result_binary = binary_search(arr, target)
time_binary = time.time() - start_time
print(f"   Результат: {result_binary} (не найден)")
print(f"   Время: {time_binary:.6f} сек")

# Линейный поиск
print("\n2. Линейный поиск (O(n)):")
start_time = time.time()
result_linear = linear_search(arr, target)
time_linear = time.time() - start_time
print(f"   Результат: {result_linear} (не найден)")
print(f"   Время: {time_linear:.6f} сек")

# Встроенный оператор in (тоже линейный поиск)
print("\n3. Оператор 'in' (линейный поиск):")
start_time = time.time()
result_in = target in arr
time_in = time.time() - start_time
print(f"   Результат: {result_in}")
print(f"   Время: {time_in:.6f} сек")

print(f"\n=== ИТОГ ===")
print(f"Бинарный поиск быстрее линейного в {time_linear/time_binary:.0f} раз!")
print(f"Логарифмическое время O(log n) против линейного O(n)")
print(f"log₂({n}) ≈ {n.bit_length()} сравнений vs {n} сравнений")