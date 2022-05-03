import math


class Point:
    """
    Representação de um ponto em um espaço 2D.
    Atributos: x, y.
    """

    def __init__(self):
        self.x = None
        self.y = None

    def print_point(p):
        print(f'({p.x}, {p.y})')

    def distancia_entre_pontos(p):
        print(f'{p.y - p.x}')


blank = Point()
blank.x = 3.0
blank.y = 5.0

# print(blank.x)
# distancia = math.sqrt((blank.x ** 2 + blank.y ** 2))
# print(distancia)
blank.print_point()
blank.distancia_entre_pontos()


class Rectangle:
    """Represents a rectangle.
    attributes: width(largura), height(altura), corner(angulo).
    """


box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0
