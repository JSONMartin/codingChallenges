# Triangle: Array of Points [(x, y), ...]

import math
def triangle_perimeter(triangle):
    distance = math.hypot(triangle.b.x - triangle.a.x, triangle.b.y - triangle.a.y) + \
    math.hypot(triangle.c.x - triangle.b.x, triangle.c.y - triangle.b.y) + \
    math.hypot(triangle.c.x - triangle.a.x, triangle.c.y - triangle.a.y)
    return distance