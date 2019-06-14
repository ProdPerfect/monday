#!/usr/bin/env python3
from setuptools import setup

from workstreams import __author__, __email__, __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='workstreams',
      version=__version__,
      description='A Python client library for Workstreams.ai',
      long_description=long_description,
      long_description_content_type='text/markdown; charset=UTF-8',
      author=__author__,
      author_email=__email__,
      packages=['workstreams', 'workstreams.resources'],
      url='https://github.com/ProdPerfect/workstreams',
      include_package_data=True,
      zip_safe=False,
      license='MIT',
      python_requires='>=3.6',
      install_requires=[
          'requests>=2.19.0'
      ],
      classifiers=[
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Operating System :: OS Independent",
      ])
