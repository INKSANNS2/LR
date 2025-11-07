fru = {
    "яблоки": 5,
    "бананы": 3,
    "апельсины": 10,
    "арбузы": 33
}
print("Начальное количество фруктов:")
for fruit, count in fru.items():
    print(f"За прилавком есть {count} {fruit}")
fru["яблоки"] -= 2
fru["арбузы"] = 0
print("\nИтоговое количество фруктов:")
for fruit, count in fru.items():
    print(f"За прилавком осталось {count} {fruit}")