
from models.point import Point
from functions.simple_line import get_points_by_slope
from functions.bresenhams_algo import bresenham
from functions.midpoint_algo import midpoint_algo
from functions.circle import four_way_symmetry


# p1 = Point(9, 18)
# p2 = Point(14, 22)
# print(get_points_by_slope(p1, p2))

# p1 = Point(9, 18)
# p2 = Point(14, 22)
# print(bresenham(p1, p2))


# p1 = Point(4, 8)
# p2 = Point(9, 12)
# midpoint_algo(p1, p2)


four_way_symmetry(0, 0, 5)
