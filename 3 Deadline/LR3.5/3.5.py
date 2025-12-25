import sys

# Функция, создающая список
def create_list(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result

# Функция, создающая генератор
def create_gen(n):
    return (i ** 2 for i in range(n))

# Тестируем
n = 1000000

lst = create_list(n)
gen = create_gen(n)

print("Сравнение использования памяти:")
print(f"Размер списка: {sys.getsizeof(lst)} байт")
print(f"Размер генератора: {sys.getsizeof(gen)} байт")

# Демонстрация работы генератора
print("\nДемонстрация генератора (первые 5 значений):")
gen2 = create_gen(10)
for i, value in enumerate(gen2):
    print(f"  {i}² = {value}")
    if i >= 4:
        break

# 1. Список (create_list) имеет пространственную сложность O(n) - 
#    он хранит все n элементов в памяти одновременно.
# 2. Генератор (create_gen) имеет пространственную сложность O(1) - 
#    он хранит только текущее состояние и не хранит все элементы.
# Генератор вычисляет значения "на лету" и более эффективен по памяти,
# но не позволяет обращаться к элементам по индексу.