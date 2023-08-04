#!/usr/bin/env python3

from setuptools import setup



setup(
    name='biostrings',
    version='0.0.1',
    author='Javier Montalvo-Arredondo',
    author_email='buitrejma@gmail.com',
    py_modules=['biostrings.biostr'],
    packages=['biostrings'],
    python_requires='>=3.9',
    description='Python wrapper for C Shared Object Library with functions to create a DNA data structure like in R Biosrtiring package. And also, this python package has some other functions to filter, splits sequences and write them to a file.',
    long_description = open('README.md', 'r').read(),
    install_requires =['ctypes'],
    license = 'GNU General Public License v3 or later (GPLv3+)',
    url='https://www.github.com/exseivier/not-alike',
    classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.11',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        ],
    include_package_data=True
        )
