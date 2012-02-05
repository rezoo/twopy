# -*- coding: utf-8 -*-

import unittest
from twopy.board import make_subject_url


class TestBoardModule(unittest.TestCase):
    def test_make_subject_url(self):
        self.assertEqual(
            make_subject_url("http://engawa.2ch.net/news/"),
            "http://engawa.2ch.net/news/subject.txt")
        self.assertEqual(
            make_subject_url("http://engawa.2ch.net/news"),
            "http://engawa.2ch.net/news/subject.txt")
