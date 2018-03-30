===============
timezonefinderL
===============

.. image:: https://img.shields.io/travis/MrMinimal64/timezonefinderL.svg?branch=master
    :target: https://travis-ci.org/MrMinimal64/timezonefinderL

.. image:: https://img.shields.io/pypi/wheel/timezonefinderL.svg
    :target: https://pypi.python.org/pypi/timezonefinderL

.. image:: https://img.shields.io/pypi/v/timezonefinderL.svg
    :target: https://pypi.python.org/pypi/timezonefinderL


timezonefinderL is the faster and lightweight, but outdated version of the original `timezonefinder <https://github.com/MrMinimal64/timezonefinder>`__. 
The data takes up 9MB (instead of 19,5MB as with the previous ``tz_world`` data).
Around 56% of the coordinates of all timezone polygons have been simplified and around 60% of the polygons (e.g. small islands) have then been included in the simplified polygons.


NOTE: The underlying data is outdated, because the ``tz_world`` data set this package was build on is not being maintained any more. Use this package in favour of ``timezonefinder`` when size and speed matter more you than actuality.

NOTE: As in the new version of ``timezonefinder`` the timezone polygons do not follow the shorelines (the borders of a timezone are simplified when there is no directly neighbouring timezone). As a consequence the results of the functions **certain_timezone_at()** and **closest_timezone_at()** are not really meaningful!


For a visualisation of the results (e.g. shapes of polygons) check out the GUI and API at: `TimezonefinderL GUI <http://timezonefinder.michelfe.it/gui>`__

For everything else please refer to the original `DOCUMENTATION <https://github.com/MrMinimal64/timezonefinder>`__.

Of course the commands need to modified:

::

    pip install timezonefinderL
    from timezonefinderL import TimezoneFinder
    ...



Also see:
`GitHub <https://github.com/MrMinimal64/timezonefinderL>`__,
`PyPI <https://pypi.python.org/pypi/timezonefinderL/>`__
