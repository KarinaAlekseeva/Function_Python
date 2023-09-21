def rectangle_area(width, height):
    result = width * height
    return result
width = float(input("Введите ширину: "))
height = float(input("Введите высоту: "))
print("Площадь прямоугольника: ", rectangle_area(width, height))