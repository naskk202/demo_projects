from math import pi
figure = str(input())
if figure == str("square"):
    square_side = float(input())
    square_face = square_side * square_side
    print(square_face)
if figure == str("triangle"):
    w = float(input())
    h = float(input())
    triangle_face = (w * h) / 2
    print (triangle_face)
if figure == str("rectangle"):
    a = float(input())
    b = float(input())
    rectangle_face = a * b
    print(rectangle_face)
if figure == str("circle"):
    r = float(input())
    circle_face = pi * (r * r)
    print (circle_face)
else:
    print("Incorect figure")