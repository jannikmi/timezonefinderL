# -*- coding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import os
import re

from setuptools import setup


def get_version(package):
    """
    Return package version as listed in `__version__` in `__init__.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version('timezonefinderL')

with open('README.rst') as f:
    readme = f.read()

with open('CHANGELOG.rst') as changelog_file:
    changelog = changelog_file.read()

native_string_pckg_name = 'timezonefinderL'

setup(
    name='timezonefinderL',
    version=version,
    packages=['timezonefinderL'],
    package_data={
        native_string_pckg_name: ['shortcuts_unique_id.bin',
                                  'timezone_names.json'],
    },
    description='lightweight python package for finding the timezone of any point on earth (coordinates) ',
    author='J. Michelfeit',
    author_email='python@michelfe.it',
    license='MIT licence',
    url='https://github.com/MrMinimal64/timezonefinderL',  # use the URL to the github repo
    keywords='timezone coordinates latitude longitude location pytzwhere tzwhere',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Localization',
    ],
    long_description=readme + '\n\n' + changelog,
    install_requires=[
        'numpy',
        'importlib_resources',
    ],
)
