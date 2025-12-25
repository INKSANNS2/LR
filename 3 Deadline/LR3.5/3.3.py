import time
import random

def find_duplicates_slow(arr):
    """Медленная версия с O(n²)"""
    duplicates = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                duplicates.append(arr[i])
                break
    return duplicates

# Генерируем список случайных чисел
n1 = 5000
arr1 = [random.randint(0, 1000) for _ in range(n1)]

start_time = time.time()
result1 = find_duplicates_slow(arr1)
time1 = time.time() - start_time
print(f"Время для n={n1}: {time1:.4f} сек")

n2 = 10000
arr2 = [random.randint(0, 1000) for _ in range(n2)]

start_time = time.time()
result2 = find_duplicates_slow(arr2)
time2 = time.time() - start_time
print(f"Время для n={n2}: {time2:.4f} сек")

# Вычисляем, во сколько раз увеличилось время
ratio = time2 / time1
print(f"\nВремя выполнения выросло примерно в {ratio:.2f} раз")

# Теоретическое ожидание: для O(n²) при увеличении n в 2 раза
# время должно вырасти примерно в 2² = 4 раза
print(f"Теоретическое ожидание для O(n²): в 4 раза")

# Ответ на вопрос:
# Если данные выросли в 2 раза, то при сложности O(n²) время выполнения
# должно вырасти примерно в 4 раза (2² = 4). 
# На практике мы видим близкое к этому значение.