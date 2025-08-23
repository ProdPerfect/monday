#!/usr/bin/env python3
from setuptools import setup

# Avoid importing the package at setup time to prevent import-time dependencies
version_meta: dict = {}
with open("monday/__version__.py", "r", encoding="utf-8") as vf:
    exec(vf.read(), version_meta)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="monday",
    version=version_meta.get("__version__", "0.0.0"),
    description="A Python client library for Monday.com",
    long_description=long_description,
    long_description_content_type="text/markdown; charset=UTF-8",
    author=version_meta.get("__author__", ""),
    author_email=version_meta.get("__email__", ""),
    packages=["monday", "monday.resources", "monday.graphqlclient"],
    url="https://github.com/ProdPerfect/monday",
    include_package_data=True,
    zip_safe=False,
    license="BSD",
    install_requires=[
        "requests>=2.30.0",
    ],
    python_requires=">=3.11",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
    ],
)
