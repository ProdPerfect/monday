#!/usr/bin/env python3
from setuptools import setup

__version__ = '2.0.0rc3'
__author__ = 'Christina D\'Astolfo'
__email__ = 'chdastolfo@gmail.com, lemi@prodperfect.com, pevner@prodperfect.com'

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='monday',
      version=__version__,
      description='A Python client library for Monday.com',
      long_description=long_description,
      long_description_content_type='text/markdown; charset=UTF-8',
      author=__author__,
      author_email=__email__,
      packages=['monday', 'monday.resources', 'monday.graphqlclient'],
      url='https://github.com/ProdPerfect/monday',
      include_package_data=True,
      zip_safe=False,
      license='BSD',
      python_requires='>=3.6',
      install_requires=[
          'requests'
      ],
      classifiers=[
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Operating System :: OS Independent",
      ])
