students = [
    ("Анна", 21, 4.5),
    ("Петр", 19, 3.2),
    ("Мария", 19, 4.8),
    ("Иван", 21, 2.1),
    ("Ольга", 22, 4.6)
]
print("Студенты старше 20 лет:")
for student in students:
    name, age, score = student
    if age > 20:
        print(f"{name} ({age}), средний балл: {score}")
best_student = students[0]
for student in students:
    if student[2] > best_student[2]:
        best_student = student
print(f"\nЛучший студент: {best_student[0]}, средний балл: {best_student[2]}")
print("\nОтсортированный список студентов:")
sorted_students = students.copy()
n = len(sorted_students)
for i in range(n):
    for j in range(0, n - i - 1):
        if sorted_students[j][0] > sorted_students[j + 1][0]:
            sorted_students[j], sorted_students[j + 1] = sorted_students[j + 1], sorted_students[j]
for student in sorted_students:
    print(f"{student[0]}, возраст: {student[1]}, балл: {student[2]}")