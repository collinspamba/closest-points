"""calculate.py
Module where closest points calculation is performed
"""
import math


def closest_pair(points_string):
    """Calculate the closest pair.
    points_string is a validated string containing tuples e.g. (2,3),(1.8,99),...
    """
    # get points in a list
    points_list = generate_tuples_list_from_string(points_string)

    # here we have a list containing tuples like (1,2),(3,4)
    # go through each tuple and calculate the distance with other tuples in the list
    distances = []
    for p,x in enumerate(points_list):
        for q,y in enumerate(points_list):
            # skip if p is q
            if p == q:
                continue

            # get the distance
            distance = get_distance(x,y)

            # append to distances
            distances.append({
                'p': p,
                'q': q,
                'distance': distance
            })

    # now sort distances by distance
    distances_sorted = sorted(distances, key=lambda d: d.get('distance'))

    # get the respective points_list items for distances_sorted's first item (lowest distance)
    closest = points_list[distances_sorted[0]['p']], points_list[distances_sorted[0]['q']]
    return str(closest[0]) + ',' + str(closest[1])

def generate_tuples_list_from_string(points_string):
    """Take a string of points and return a list containing the tuples
    """
    # strip out the brackets and split by ','
    # this should give us a list with individual items e.g. [1,2,3,4,...]
    delta=points_string.replace('(', '').replace(')','').split(',')

    # for every element in this list ensure it can be converted to a float
    final = []
    for i in delta:
        try:
            item = float(i)
            if item.is_integer():
                final.append(int(i))
            else:
                final.append(item)
        except ValueError:
            return False # so that vaildation by the serializer fails

    # collect element pairs in the list into tuples
    points_list = list(zip(final[0::2], final[1::2]))
    return points_list

def get_distance(p,q):
    """Calculate the distance between points p and q.
    p and q are validated tuples e.g. (942,42),(1.4,93)
    """
    # formula for calculating distance between p and q
    distance = math.sqrt(square(q[0] - p[0]) + square(q[1] - p[1]))
    return distance

def square(x):
    """Return the square of a number
    """
    return x*x
