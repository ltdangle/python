def triangle_area(x1: float, y1:float, x2:float, y2:float, x3:float, y3:float)->float:
    return (1/2) * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))


print(triangle_area(2, 3, 5, 11, 9, 5))
