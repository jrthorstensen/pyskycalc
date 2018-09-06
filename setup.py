"""
Time-and-the-sky routines for astronomers, built mostly on astropy and including a GUI interface.

Copyright 2018 by John Thorstensen. Distributed under a BSD-style 3-clause license.
"""

###################################################################################
#                            SOME DOCUMENTATION                                   #
###################################################################################
# This file is used to create the package itself,
# the setup function has all the meta-information (like author, version, name, etc)
# and the package information (where to find the .py files, scripts and .dat files)
#
# Using `python setup.py build install` the script installs the package in the
# python system.
#
# To create an `pip` installable file the command `python setup.py bdist_wheel`
# is used to create a wheel file in the "dist" folder that can be installed with
# `pip install file.whl` or upload to pypi using twine (pip installable tool)
#
#################################################################################


# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
from io import open

#Reading README.me for detailed information
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

#Main function for packaging
setup(
    #Meta Information
    name='pyskycalc',
    version='0.1.0',
    description='Time-and-the-sky routines for astronomers, built mostly on astropy and including a GUI interface.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/jrthorstensen/pyskycalc',
    author='John Thorstensen',
    author_email='john.r.thorstensen@dartmouth.edu',
    #Package information
    packages=['pyskycalc'], #Package name
    package_data={'pyskycalc': ['data/*.dat']}, # Data directory
    scripts=['bin/pyskycalcgui'], # Scripts installed to /usr/local/bin
    install_requires = ['numpy > 1.8','astropy > 2.0'], # Package requried to run
    # More meta information (optional)
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Astronomers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='astronomy',
)
