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
    for p in points_list:
        for q in points_list:
            # skip if p is q
            if points_list.index(p) == points_list.index(q):
                continue

            # check if we have already calculated for these two points
            exists = False
            for d in distances:
                if (d.get('p') or d.get('p') == 0) and (d.get('q') or d.get('q') == 0):
                    if d['p'] == points_list.index(q) and d['q'] == points_list.index(p):
                        exists = True
                    if d['q'] == points_list.index(p) and d['p'] == points_list.index(q):
                        exists = True

            if exists:
                continue

            # get the distance
            distance = get_distance(p,q)

            # append to distances
            distances.append({
                'p': points_list.index(p),
                'q': points_list.index(q),
                'distance': distance
            })

    # now sort distances by distance
    distances_sorted = sorted(distances, key=lambda d: d.get('distance'))

    # get the respective points_list items for distances_sorted's first item (lowest distance)
    return points_list[distances_sorted[0]['p']], points_list[distances_sorted[0]['q']]

def generate_tuples_list_from_string(points_string):
    """Take a string of points and return a list containing the tuples
    """
    # strip out the brackets and split by ','
    # this should give us a list with individual items e.g. [1,2,3,4,...]
    delta=points_string.replace('(', '').replace(')','').split(',')

    # collect element pairs in the list into tuples
    points_list = list(zip(delta[0::2], delta[1::2]))
    return points_list

def get_distance(p,q):
    """Calculate the distance between points p and q.
    p and q are validated tuples e.g. (942,42),(1.4,93)
    """
    # formula for calculating distance between p and q
    distance = math.sqrt(square(float(q[0]) - float(p[0])) + square(float(q[1]) - float(p[1])))
    return distance

def square(x):
    """Return the square of a number
    """
    return x*x
