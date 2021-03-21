#
# helper functions for common requirements for line algorithms
#

# @params:  {Points}
# @returns: {interger} - Slope
def get_slope(p1, p2):
    return (p2.y - p1.y)/(p2.x - p1.x)


