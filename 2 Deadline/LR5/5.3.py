colors = {
    "красный": (255, 0, 0),
    "зеленый": (0, 255, 0),
    "синий": (0, 0, 255),
    "белый": (255, 255, 255),
    "черный": (0, 0, 0),
    "желтый": (255, 255, 0),
    "фиолетовый": (128, 0, 128)
}
print("Смешивание цветов:")
color1 = colors["красный"]
color2 = colors["синий"]
mixed_color = (
    (color1[0] + color2[0]) // 2,
    (color1[1] + color2[1]) // 2,
    (color1[2] + color2[2]) // 2
)
print(f"Красный {color1} + Синий {color2} = Фиолетовый {mixed_color}")
print("\nИнвертирование цвета:")
original_color = colors["белый"]
inverted_color = (
    255 - original_color[0],
    255 - original_color[1],
    255 - original_color[2]
)
print(f"Белый {original_color} - Черный {inverted_color}")
print("\nВсе цвета в палитре:")
for color_name, rgb in colors.items():
    print(f"{color_name}: {rgb}")