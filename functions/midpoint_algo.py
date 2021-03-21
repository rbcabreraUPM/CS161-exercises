#
# https://www.gatevidyalay.com/mid-point-line-drawing-algorithm/
#
#
import math
from helper.lines import get_slope
import matplotlib.pyplot as plt


def midpoint_algo(p1, p2):
    x_array = []
    y_array = []
    # step  1:
    delta_y = p2.y - p1.y
    delta_x = p2.x - p1.x

    # step 2:
    pk = 2 * delta_y - delta_x
    delta_pk = 2 * (delta_y - delta_x)

    # step 3
    x = p1.x
    y = p1.y

    print(
        'delta x:', delta_x,
        ' delta_y:', delta_y,
        ' pk: ', pk,
        ' delta_pk: ', delta_pk,)

    x_array.append(x)
    y_array.append(y)
    while x < p2.x:
        if pk < 0:
            pk = pk = pk + 2 * delta_y
        else:
            y = y + 1
            pk = pk + delta_pk
        x = x + 1
        print(
            ' pk: ', pk,
            ' x:', x,
            ' y:', y,)
        x_array.append(x)
        y_array.append(y)

    x_array.append(p2.x)
    y_array.append(p2.y)
    plt.scatter(x_array, y_array)
    plt.plot(x_array, y_array)
    plt.grid()
    plt.title('Bresenham')
    plt.show()
