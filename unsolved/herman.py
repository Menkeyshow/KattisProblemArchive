import math
r = int(input())

def taxicab_geo(radius):
    # taxicab circle: |x| + |y| = 1
    #  ==> pi = 4 !!
    t1 = (0,0)
    t2 = (0, radius)

    return (abs(t1[0] - t2[0]) + abs(t1[1] - t2[1]))

def area_of_circle(radius):
    return math.pi * radius**2

def area_of_circle_taxicab(radius):
    return (4 * radius**2) / 2

print(area_of_circle(r))
print(area_of_circle_taxicab(r))