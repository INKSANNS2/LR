products = {
    "Ноутбук": {"price": 50000, "sold": 15},
    "Мышь": {"price": 1000, "sold": 45},
    "Клавиатура": {"price": 2500, "sold": 30},
    "Монитор": {"price": 30000, "sold": 8}
}
max_sold = 0
max_sold_product = ""
for product_name, product_info in products.items():
    if product_info["sold"] > max_sold:
        max_sold = product_info["sold"]
        max_sold_product = product_name
print(f"Самый продаваемый товар: {max_sold_product} ({max_sold} шт)")
total = 0
for product_name, product_info in products.items():
    product = product_info["price"] * product_info["sold"]
    total += product
print(f"Общая выручка: {total} руб.")
max = 0
max_product = ""
for product_name, product_info in products.items():
    product = product_info["price"] * product_info["sold"]
    
    if product > max:
        max = product
        max_product = product_name
print(f"Товар с наибольшей выручкой: {max_product} ({max} руб)")
print("\nВыручка по каждому товару:")
for product_name, product_info in products.items():
    revenue = product_info["price"] * product_info["sold"]
    print(f"{product_name}: {revenue} руб.")