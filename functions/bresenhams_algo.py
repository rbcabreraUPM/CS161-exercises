#
# https://www.gatevidyalay.com/bresenham-line-drawing-algorithm/
#
#
import math
from helper.lines import get_slope
import matplotlib.pyplot as plt


def bresenham(p1, p2):
    x_array = []
    y_array = []

    # step  1:
    delta_y = p2.y - p1.y
    delta_x = p2.x - p1.x

    # step 2: calculate the decision parameter
    pk = 2 * delta_y - delta_x
    print('delta x:', delta_x, ' delta_y:', delta_y, ' decision param: ', pk,)
    # step 3

    x = p1.x
    y = p1.y
    while x < p2.x:
        x_array.append(x)
        y_array.append(y)
        print(pk, x, y)
        if pk < 0:
            pk = pk + 2 * delta_y
        else:
            y = y + 1
            pk = pk + (2 * delta_y) - (2 * delta_x)

        x = x + 1

    x_array.append(p2.x)
    y_array.append(p2.y)
    plt.scatter(x_array, y_array)
    plt.plot(x_array, y_array)
    plt.grid()
    plt.title('Bresenham')
    plt.show()
