def x_point(x1, x2):
    if abs(x1) > abs(x2):
        return int(x2)
    return int(x1)


def y_point(y1, y2):
    if abs(y1) > abs(y2):
        return int(y2)
    return int(y1)

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(f"({x_point(x1, x2)}, {y_point(y1, y2)})")