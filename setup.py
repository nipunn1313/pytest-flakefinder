#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-flakefinder',
    version='0.1.0',
    author='David Euresti',
    author_email='david@dropbox.com',
    maintainer='David Euresti',
    maintainer_email='david@dropbox.com',
    license='MIT',
    url='https://github.com/deuresti/pytest-flakefinder',
    description='Runs tests multiple times to expose flakiness.',
    long_description=read('README.rst'),
    py_modules=['pytest_flakefinder'],
    install_requires=['pytest>=2.7.2'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'flakefinder = pytest_flakefinder',
        ],
    },
)