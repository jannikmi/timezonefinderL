# -*- coding:utf-8 -*-
from math import floor

from numpy import int64

from .global_settings import COORD2INT_FACTOR, INT2COORD_FACTOR


def inside_polygon(x, y, coordinates):
    """
    Implementing the ray casting point in polygon test algorithm
    cf. https://en.wikipedia.org/wiki/Point_in_polygon#Ray_casting_algorithm
    :param x:
    :param y:
    :param coordinates: a polygon represented by a list containing two lists (x and y coordinates):
        [ [x1,x2,x3...], [y1,y2,y3...]]
        those lists are actually numpy arrays which are bei
        ng read directly from a binary file
    :return: true if the point (x,y) lies within the polygon

    Some overflow considerations for the critical part of comparing the line segment slopes:

        (y2 - y) * (x2 - x1) <= delta_y_max * delta_x_max
        (y2 - y1) * (x2 - x) <= delta_y_max * delta_x_max
        delta_y_max * delta_x_max = 180 * 360 < 65 x10^3

    Instead of calculating with float I decided using just ints (by multiplying with 10^7). That gives us:

        delta_y_max * delta_x_max = 180x10^7 * 360x10^7
        delta_y_max * delta_x_max <= 65x10^17

    So these numbers need up to log_2(65 x10^17) ~ 63 bits to be represented! Even though values this big should never
     occur in practice (timezone polygons do not span the whole lng lat coordinate space),
     32bit accuracy hence is not safe to use here!
     Python 2.2 automatically uses the appropriate int data type preventing overflow
     (cf. https://www.python.org/dev/peps/pep-0237/),
     but here the data types are numpy internal static data types. The data is stored as int32
     -> use int64 when comparing slopes!
    """
    contained = False
    # the edge from the last to the first point is checked first
    i = -1
    y1 = coordinates[1][-1]
    y_gt_y1 = y > y1
    for y2 in coordinates[1]:
        y_gt_y2 = y > y2
        if y_gt_y1:
            if not y_gt_y2:
                x1 = coordinates[0][i]
                x2 = coordinates[0][i + 1]
                # only crossings "right" of the point should be counted
                x1GEx = x <= x1
                x2GEx = x <= x2
                # compare the slope of the line [p1-p2] and [p-p2]
                # depending on the position of p2 this determines whether the polygon edge is right or left of the point
                # to avoid expensive division the divisors (of the slope dy/dx) are brought to the other side
                # ( dy/dx > a  ==  dy > a * dx )
                # int64 accuracy needed here!
                if (x1GEx and x2GEx) or ((x1GEx or x2GEx)
                                         and (int64(y2) - int64(y)) * (int64(x2) - int64(x1)) <= (
                                             int64(y2) - int64(y1)) * (int64(x2) - int64(x))):
                    contained = not contained

        else:
            if y_gt_y2:
                x1 = coordinates[0][i]
                x2 = coordinates[0][i + 1]
                # only crossings "right" of the point should be counted
                x1GEx = x <= x1
                x2GEx = x <= x2
                if (x1GEx and x2GEx) or ((x1GEx or x2GEx)
                                         and (int64(y2) - int64(y)) * (int64(x2) - int64(x1)) >= (
                                             int64(y2) - int64(y1)) * (int64(x2) - int64(x))):
                    contained = not contained

        y1 = y2
        y_gt_y1 = y_gt_y2
        i += 1

    return contained


def int2coord(i4):
    return float(i4 * INT2COORD_FACTOR)


def coord2int(double):
    return int(double * COORD2INT_FACTOR)


def coord2shortcut(lng, lat):
    return int(floor((lng + 180))), int(floor((90 - lat) * 2))


def rectify_coordinates(lng, lat):
    if lng > 180.0 or lng < -180.0 or lat > 90.0 or lat < -90.0:
        raise ValueError(b'The coordinates should be given in degrees. They are out ouf bounds.')

    # coordinates on the rightmost (lng=180) or lowest (lat=-90) border of the coordinate system
    # are not included in the shortcut lookup system
    # always (only) the "top" and "left" borders belong to a shortcut
    if lng == 180.0:
        # a longitude of 180.0 is not allowed, because the right border of a shortcut
        # is already considered to lie within the next shortcut
        # it however equals lng=0.0 (earth is a sphere)
        lng = 0.0

    if lat == -90.0:
        # a latitude of -90.0 (=exact south pole) corresponds to just one single point on earth
        # and is not allowed, because bottom border of a shortcut is already considered to lie within the next shortcut
        # it has the same timezones as the points with a slightly higher latitude
        lat += INT2COORD_FACTOR  # adjust by the smallest possible amount

    return lng, lat


def convert2coords(polygon_data):
    # return a tuple of coordinate lists
    return [[int2coord(x) for x in polygon_data[0]], [int2coord(y) for y in polygon_data[1]]]


def convert2coord_pairs(polygon_data):
    # return a list of coordinate tuples (x,y)
    coodinate_list = []
    i = 0
    for x in polygon_data[0]:
        coodinate_list.append((int2coord(x), int2coord(polygon_data[1][i])))
        i += 1
    return coodinate_list
