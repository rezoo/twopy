# -*- coding: utf-8 -*-

import unittest
from thread_test import TestThreadModule


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TestThreadModule))
    return suite
