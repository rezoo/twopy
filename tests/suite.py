# -*- coding: utf-8 -*-

import unittest
from thread_test import TestThreadModule
from board_test import TestBoardModule


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TestThreadModule))
    suite.addTests(unittest.makeSuite(TestBoardModule))
    return suite
