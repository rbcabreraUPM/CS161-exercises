# 4 way symmetry
from models.point import Point
import math
import matplotlib.pyplot as plt

#
# http://www.vrarchitect.net/anu/cg/Circle/symmetry4.en.html
# http://groups.csail.mit.edu/graphics/classes/6.837/F98/Lecture6/circle.html


def four_way_symmetry(xCenter, yCenter, rad):
    r2 = rad ** 2
    point_arr = []

    point_arr.append(Point(xCenter, yCenter + rad))
    point_arr.append(Point(xCenter, yCenter - rad))

    x = 1
    while(x <= rad):
        y = int(math.sqrt(r2 - x**2) + 0.5)
        point_arr.append(Point(xCenter + x, yCenter + y))
        point_arr.append(Point(xCenter + x, yCenter - y))
        point_arr.append(Point(xCenter - x, yCenter + y))
        point_arr.append(Point(xCenter - x, yCenter - y))
        x = x + 1

    x_array = [point.x for point in point_arr]
    y_array = [point.y for point in point_arr]
    plt.scatter(x_array, y_array)
    plt.grid()
    plt.title('4 way Symmetry')
    plt.show()


def eight_way_symmetry():
    return 'assignment nyo na to :)'
