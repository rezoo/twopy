# -*- coding: utf-8 -*-

import unittest
from twopy.thread import make_dat_url, make_thread_url


class TestThreadModule(unittest.TestCase):
    def test_make_thread_url(self):
        result = make_thread_url("http://engawa.2ch.net/news/", "1234.dat")
        self.assertEqual(
            result,
            "http://engawa.2ch.net/test/read.cgi/news/1234/")
        result = make_thread_url("http://engawa.2ch.net/news", "456789.dat")
        self.assertEqual(
            result,
            "http://engawa.2ch.net/test/read.cgi/news/456789/")

    def test_make_dat_url(self):
        result = make_dat_url("http://engawa.2ch.net/news/", "1234.dat")
        self.assertEqual(result, "http://engawa.2ch.net/news/dat/1234.dat")
        result = make_dat_url("http://engawa.2ch.net/news", "456789.dat")
        self.assertEqual(result, "http://engawa.2ch.net/news/dat/456789.dat")
