from helper.lines import get_slope

# @params: {Points}
# @response: String na walang kianlaman sa 161


def get_points_by_slope(p1, p2):
    m = get_slope(p1, p2)
    y = p1.y + 0.5
    for x in range(p1.x, p2.x):
        print(x, y)
        y = y + m

    return 'hirap aralin ng 161 lec'
