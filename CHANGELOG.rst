Changelog
=========


Deprecation (2020-05-12)
------------------

This package has been deprecated.
Use the ``TimezoneFinderL`` class of the `timezonefinder <https://github.com/MrMinimal64/timezonefinder>`__ package instead.


4.0.2 (2019-06-23)
------------------

* MAJOR UPDATE: only the function ``timezone_at()`` is being supported
* not based on the simplification of the timezone polygons any more (not easily achievable with the new boundary data set)
* use the precomputed shortcuts to instantly look up a timezone ("instant shortcut", most common zone of the polygons within that shortcut)
* updated the code to the status of the current ``timezonefinder`` main package ``v4.0.2``
* data in use now is `timezone-boundary-builder 2019a <https://github.com/evansiroky/timezone-boundary-builder/releases/tag/2019a>`__
* described options for increasing the accuracy in readme
* dropped python2 support


2.0.1 (2017-04-08)
------------------

* added missing package data entries (2.0.0 didn't include all necessary .bin files)


2.0.0 (2017-04-07)
------------------

* introduction of this version of `timezonefinder <https://github.com/MrMinimal64/timezonefinder/>`__
* data has been simplified which affects speed and data size. Around 56% of the coordinates of the timezone polygons have been deleted and around 60% of the polygons (mostly small islands) have been included in the simplified polygons. For any coordinate on landmass the results should stay the same, but accuracy at the shorelines is lost. This eradicates the usefulness of closest_timezone_at() and certain_timezone_at() but the main use case for this package (= determining the timezone of a point on landmass) is improved.
* file_converter.py has been complemented and modified to perform those simplifications
* introduction of new function get_geometry() for querying timezones for their geometric shape
* added shortcuts_unique_id.bin for instantly returning an id if the shortcut corresponding to the coords only contains polygons of one zone
* data is now stored in separate binaries for ease of debugging and readability
* polygons are stored sorted after their timezone id and size
* timezonefinder can now be called directly as a script (experimental with reduced functionality, see readme)
* optimisations on point in polygon algorithm
* small simplifications in the helper functions
* clarification of the readme
* clarification of the comments in the code
* referenced the new conda-feedstock in the readme
* referenced the new timezonefinder API/GUI


for older versions refer to `timezonefinder <https://github.com/MrMinimal64/timezonefinder/>`__.
