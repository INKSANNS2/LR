import time
import random

# Медленное решение O(n²)
def find_pair_slow(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return (arr[i], arr[j])
    return None

# Быстрое решение O(n)
def find_pair_fast(arr, target):
    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen:  # O(1) для set
            return (complement, num)
        seen.add(num)
    return None

# Генерируем тестовые данные
n = 10000
arr = [random.randint(1, 10000) for _ in range(n)]
target = random.randint(10000, 15000)

print("Тестирование на списке из", n, "элементов")
print("Цель:", target)

# Тестируем медленную версию
start_time = time.time()
result_slow = find_pair_slow(arr, target)
time_slow = time.time() - start_time
print(f"\nМедленный алгоритм (O(n²)):")
print(f"Результат: {result_slow}")
print(f"Время: {time_slow:.4f} сек")

# Тестируем быструю версию
start_time = time.time()
result_fast = find_pair_fast(arr, target)
time_fast = time.time() - start_time
print(f"\nБыстрый алгоритм (O(n)):")
print(f"Результат: {result_fast}")
print(f"Время: {time_fast:.4f} сек")

print(f"\nУскорение: в {time_slow/time_fast:.1f} раз!")
print("Быстрая версия использует set для хранения уже просмотренных чисел,")
print("что позволяет проверять наличие дополнения за O(1) вместо O(n).")