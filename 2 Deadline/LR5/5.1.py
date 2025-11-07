from math import sqrt
point_a = (17, 7)
point_b = (3, 1.97)
x1, y1 = point_a
x2, y2 = point_b
dist = sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Точка A: {point_a}")
print(f"Точка B: {point_b}")
print(f"Расстояние между точками: {dist:.2f}")