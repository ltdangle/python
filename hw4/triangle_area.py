def triangle_area(x1, y1, x2, y2, x3, y3):
    return (1/2) * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))


print(triangle_area(2, 3, 5, 11, 9, 5))
