#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import sys
sys.path.append("./tests")

setup(
    name="twopy",
    version="0.8",
    url="http://mglab.blogspot.com/",
    packages=find_packages(),
    test_suite="suite.suite"
)
