def process_orders(stock, orders):
    # Копируем склад
    new_stock = [item.copy() for item in stock]
    revenue = 0
    cancelled = []
    
    # Обрабатываем каждый заказ
    for order in orders:
        order_id = order["id"]
        order_count = order["count"]
        found = False
        
        # Ищем товар
        for item in new_stock:
            if item["id"] == order_id:
                found = True
                if item["qty"] >= order_count:
                    # Продаем
                    item["qty"] -= order_count
                    revenue += item["price"] * order_count
                else:
                    # Отменяем
                    cancelled.append(order.copy())
                break
        
        # Если не нашли - отменяем
        if not found:
            cancelled.append(order.copy())
    
    return revenue, new_stock, cancelled

# Пример
stock = [
    {"id": 1, "name": "Ноутбук", "price": 5000, "qty": 10},
    {"id": 2, "name": "Мышь", "price": 15000, "qty": 60}
]
orders = [{"id": 1, "count": 2}, {"id": 2, "count": 70}]
    
money, new_stock, bad = process_orders(stock, orders)
print(f"Выручка: {money}")
print(f"Отменено: {len(bad)}")