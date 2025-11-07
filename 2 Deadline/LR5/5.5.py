math = {"Alice", "Bob", "Charlie", "David"}
physics = {"Bob", "David", "Eve", "Frank", "Alice"}
cs = {"Alice", "Charlie", "Eve", "Grace"}
all = math & physics & cs
print(f"Все три курса: {all}")
only_math = math - physics - cs
only_physics = physics - math - cs
only_cs = cs - math - physics
one = only_math | only_physics | only_cs
print(f"Только один курс: {one}")
math_not_physics = math - physics
print(f"Математика но не физика: {math_not_physics}")
all1 = math | physics | cs
print(f"Всего студентов: {len(all1)}")
print(f"Все студенты: {all1}")
print(f"\nДополнительная информация:")
print(f"Математика и физика: {math & physics}")
print(f"Физика или CS: {physics | cs}")