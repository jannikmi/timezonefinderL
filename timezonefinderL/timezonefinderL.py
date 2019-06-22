# -*- coding:utf-8 -*-
import json
from io import SEEK_CUR, BytesIO
from os.path import abspath, join, pardir
from struct import unpack

import numpy as np
from importlib_resources import open_binary
from numpy import dtype, fromfile

from .global_settings import DTYPE_FORMAT_H, NR_BYTES_H, NR_SHORTCUTS_PER_LAT, TIMEZONE_NAMES_FILE
from .helpers import coord2shortcut, rectify_coordinates

with open(abspath(join(__file__, pardir, TIMEZONE_NAMES_FILE)), 'r') as f:
    timezone_names = json.loads(f.read())


def fromfile_memory(file, **kwargs):
    # res = np.frombuffer(file.getbuffer(), offset=file.tell(), **kwargs)
    # faster:
    res = np.frombuffer(file.getbuffer(), offset=file.tell(), **kwargs)
    file.seek(dtype(kwargs['dtype']).itemsize * kwargs['count'], SEEK_CUR)
    return res


class TimezoneFinder:
    """
    This class lets you quickly find the timezone of a point on earth.
    Only the most common zone per half degree of latitude and per degree of longitude is being stored.
    """

    def __init__(self, in_memory=False):
        self.in_memory = in_memory

        if self.in_memory:
            self.fromfile = fromfile_memory
        else:
            self.fromfile = fromfile

        # open all the files in binary reading mode
        # for more info on what is stored in which .bin file, please read the comments in file_converter.py
        self.shortcuts_unique_id = self.open_binary('timezonefinderL', 'shortcuts_unique_id.bin')

    def open_binary(self, *args):
        bin_fd = open_binary(*args)
        if self.in_memory:
            mem_bin_fd = BytesIO(bin_fd.read())
            mem_bin_fd.seek(0)
            bin_fd.close()
            return mem_bin_fd
        else:
            return bin_fd

    def __del__(self):
        self.shortcuts_unique_id.close()

    def timezone_at(self, *, lng, lat):
        """
        this function instantly returns the zone id of the most common zone within a shortcut if present
        :param lng: longitude of the point in degree (-180.0 to 180.0)
        :param lat: latitude in degree (90.0 to -90.0)
        :return: the timezone name of the most common zone or None
        """
        lng, lat = rectify_coordinates(lng, lat)
        shortcut_id_x, shortcut_id_y = coord2shortcut(lng, lat)
        self.shortcuts_unique_id.seek(
            (180 * NR_SHORTCUTS_PER_LAT * NR_BYTES_H * shortcut_id_x + NR_BYTES_H * shortcut_id_y))
        try:
            return timezone_names[unpack(DTYPE_FORMAT_H, self.shortcuts_unique_id.read(NR_BYTES_H))[0]]
        except IndexError:
            return None


if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(description='parse training parameters')
    parser.add_argument('lng', type=float, help='longitude to be queried')
    parser.add_argument('lat', type=float, help='latitude to be queried')
    parser.add_argument('-v', action='store_true', help='verbosity flag')

    # takes input from sys.argv
    parsed_args = parser.parse_args()
    tf = TimezoneFinder()
    tz = tf.timezone_at(lng=parsed_args.lng, lat=parsed_args.lat)
    if parsed_args.v:
        print('Looking for TZ at lat=', parsed_args.lat, ' lng=', parsed_args.lng)
        print('Function: timezone_at()')
        print('Timezone=', tz)
    else:
        print(tz)
