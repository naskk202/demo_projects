a = float(input())
b = float(input())
c = float(input())
square = 2 * (a * a) - 2.4
rectangle = 2 * (a * b) - 4.5
roof_front = 2 * ((a * c) /2)
roof_side = 2 *(b * a)
red_paint = (roof_front + roof_side) / 4.3
green_paint = (square + rectangle) / 3.4
print(round(green_paint, 2))
print(round(red_paint, 2))