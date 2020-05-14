===============
timezonefinderL
===============



.. warning::

    This package is deprecated.
    Use the ``TimezoneFinderL`` class of the `timezonefinder <https://github.com/MrMinimal64/timezonefinder>`__ package instead.



.. image:: https://img.shields.io/travis/MrMinimal64/timezonefinderL/master.svg
    :target: https://travis-ci.org/MrMinimal64/timezonefinderL

.. image:: https://img.shields.io/pypi/wheel/timezonefinderL.svg
    :target: https://pypi.python.org/pypi/timezonefinderL

.. image:: https://pepy.tech/badge/timezonefinderL
    :alt: Total PyPI downloads
    :target: https://pypi.python.org/pypi/timezonefinderL

.. image:: https://img.shields.io/pypi/v/timezonefinderL.svg
    :target: https://pypi.python.org/pypi/timezonefinderL


``timezonefinderL`` is the faster and lightweight, but inaccurate version of the original `timezonefinder <https://github.com/MrMinimal64/timezonefinder>`__.
Use this package in favour of ``timezonefinder`` when memory usage and speed matter more to you than accuracy.


Only the function ``timezone_at()`` is being supported and ``numba`` cannot be used for precompilation.
The commands need to modified:

::

    pip install timezonefinderL


.. code-block:: python

    from timezonefinderL import TimezoneFinder

    tf = TimezoneFinder()

    longitude, latitude = 13.358, 52.5061
    tf.timezone_at(lng=longitude, lat=latitude)  # returns 'Europe/Berlin'


For everything else please refer to the original `Documentation <https://github.com/MrMinimal64/timezonefinder>`__.


Operating Principle
-------------------

Instead of storing timezone polygons and checking which polygon a query point is included in, like with the vanilla ``timezonefinder``,
this package uses only the precomputed "shortcuts" to instantly lookup a timezone.
Shortcuts are defined by splitting the coordinate system into rectangles.
The zone which has the highest amount of timezone polygons (not covered surface!) within such a shortcut rectangle is instantly being returned.

This requires far less memory and computing time, but of course is not accurate close to the borders of two neighbouring timezones.


The size of the shortcut rectangles (<-> accuracy) is equal to the one used in the vanilla ``timezonefinder`` (1 shortcut per degree longitude, 2 per degree latitude, 260KB binary file size).
In order to increase the accuracy (more and smaller shortcut rectangles), increment the parameters ``NR_SHORTCUTS_PER_LNG`` and ``NR_SHORTCUTS_PER_LAT`` in ``global_settings.py`` and compile a new binary shortcut file by running ``file_converter.py``.


Speed Test Results:
-------------------

obtained on MacBook Pro (15-inch, 2017), 2,8 GHz Intel Core i7
It can be seen that ``timezonefinderL`` is roughly one order of magnitude faster than ``timezonefinder``:

::

    Speed Tests:
    -------------
    "realistic points": points included in a timezone

    in memory mode: False

    testing 100000 realistic points
    total time: 0.5513s
    avg. points per second: 1.8 * 10^5

    testing 100000 random points
    total time: 0.5682s
    avg. points per second: 1.8 * 10^5


    in memory mode: True

    testing 100000 realistic points
    total time: 0.1688s
    avg. points per second: 5.9 * 10^5


    testing 100000 random points
    total time: 0.1837s
    avg. points per second: 5.4 * 10^5



Contact
-------


If you notice that the tz data is outdated, encounter any bugs, have
suggestions, criticism, etc. feel free to **open an Issue**, **add a Pull Requests** on Git or ...

contact me: *[python] {*-at-*} [michelfe] {-*dot*-} [it]*



License
-------

``timezonefinderL`` is distributed under the terms of the MIT license
(see LICENSE.txt).



Also see:
`GitHub <https://github.com/MrMinimal64/timezonefinderL>`__,
`PyPI <https://pypi.python.org/pypi/timezonefinderL/>`__,
`GUI and API <http://timezonefinder.michelfe.it/gui>`__ of the outdated ``timezonefinderL``
`timezonefinder <https://github.com/MrMinimal64/timezonefinder>`__,
