temp = [15, 18, 12, 20, 16, 14, 19, 17, 13, 21, 15, 16, 18, 20]
print(f"Температуры: {temp}")
max = temp[0]
min = temp[0]
for temp1 in temp:
    if temp1 > max:
        max= temp1
    if temp1 < min:
        min = temp1
print(f"Максимальная: {max}°C")
print(f"Минимальная: {min}°C")
total = 0
for temp1 in temp:
    total += temp1
ave_temp = total / len(temp)
print(f"Средняя: {ave_temp:.1f}°C")
ave = 0
for temp1 in temp:
    if temp1 > ave_temp:
        ave += 1
print(f"Дней выше средней: {ave}")
sort= []
for temp1 in temp:
    sort.append(temp1)
n = len(sort)
for i in range(n):
    for j in range(0, n - i - 1):
        if sort[j] > sort[j + 1]:
            sort[j], sort[j + 1] = sort[j + 1], sort[j]
print(f"Отсортированные температуры: {sort}")
fahren = []
for temp1 in temp:
    fahren1 = temp1 * 9/5 + 32
print(f"Температуры в Фаренгейтах: {fahren1}")