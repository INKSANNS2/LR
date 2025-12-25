import time

lst = list(range(100000))

start_time = time.time()
for _ in range(1000):
    lst.pop(0)  
# O(n) - удаление из начала требует сдвига всех остальных элементов
end_time = time.time()
print(f"Время pop(0) (удаление из начала): {end_time - start_time:.4f} сек")

lst = list(range(100000))

start_time = time.time()
for _ in range(1000):
    lst.pop()  
# O(1) - удаление с конца не требует сдвига элементов
end_time = time.time()
print(f"Время pop() (удаление с конца): {end_time - start_time:.4f} сек")
