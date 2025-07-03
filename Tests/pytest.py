import pytest
from Netolya.Tester.main import check_triangle

@pytest.mark.parametrize(
    'side1, side2, side3, res',
    (
        (0, 0, 0, "Треугольник не существует"),
        (0, 0, 1, "Треугольник не существует"),
        (0, 1, 1, "Треугольник не существует"),
        (1, 1, 1, "Равносторонний треугольник"),
        (1, 2, 2, "Равнобедренный треугольник"),
        (1, 2, 3, "Треугольник не существует"),
        (7, 3, 5, "Треугольник разносторонний")
    )

)
def test_check_triangle(side1, side2, side3, res):
    assert check_triangle(side1, side2, side3) == res