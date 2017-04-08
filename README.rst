===============
timezonefinderL
===============

.. image:: https://img.shields.io/travis/MrMinimal64/timezonefinderL.svg?branch=master
    :target: https://travis-ci.org/MrMinimal64/timezonefinderL

.. image:: https://img.shields.io/pypi/wheel/timezonefinderL.svg
    :target: https://pypi.python.org/pypi/timezonefinderL

.. image:: https://img.shields.io/pypi/v/timezonefinderL.svg
    :target: https://pypi.python.org/pypi/timezonefinderL


timezonefinderL is the faster and lightweight version of the original `timezonefinder <https://github.com/MrMinimal64/timezonefinder>`__. 
The data takes up 9MB (instead of 19,5MB as with timezonefinder).
Around 56% of the coordinates of the timezone polygons have been simplified and around 60% of the polygons (mostly small islands) have been included in the simplified polygons.


NOTE: In contrast to ``timezonefinder`` with this package the borders of a timezone are stored simplified
when there is no directly neighbouring timezone. So on shorelines the polygons look a lot different now!
This consequently means that the functions **certain_timezone_at()** and **closest_timezone_at()** are not really useful any more!

Check out the GUI and API at: `TimezonefinderL GUI <http://timezonefinder.michelfe.it/gui>`__

For everything else please refer to the `DOCUMENTATION <https://github.com/MrMinimal64/timezonefinder>`__.

Of course the commands need to modified:

::

    pip install timezonefinderL
    from timezonefinderL import TimezoneFinder
    ...



Also see:
`GitHub <https://github.com/MrMinimal64/timezonefinderL>`__. 
`PyPI <https://pypi.python.org/pypi/timezonefinderL/>`__


License
=======

``timezonefinderL`` is distributed under the terms of the MIT license
(see LICENSE.txt).



Speed Comparison
================

::

    shapely: ON (tzwhere)
    Numba: ON (timezonefinderL)


    TIMES for  10000 realistic points
    tzwhere: 0:00:00.608965
    timezonefinder: 0:00:00.564314
    0.08 times faster


    TIMES for  10000 random points
    tzwhere: 0:00:00.650164
    timezonefinder: 0:00:00.508654
    0.28 times faster
