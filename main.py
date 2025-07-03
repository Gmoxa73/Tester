def check_triangle(side1: int, side2: int, side3: int):
    if (side1+side2) <= side3 or (side2+side3) <= side1 or (side3+side1) <= side2: # условие, что треугольник существует
        result = "Треугольник не существует"
    elif side1 == side2 and side2 == side3 and side1 == side3: # условие, что треугольник равносторонний
        result = "Равносторонний треугольник"
    elif side1 == side2 or side2 == side3 or side1 == side3: # условие, что треугольник равнобедренный
        result = "Равнобедренный треугольник"
    else: # во всех остальных случаях треугольник разносторонний
        result = "Треугольник разносторонний"
    return result

print(check_triangle(4, 2, 3))