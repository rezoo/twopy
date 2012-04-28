# -*- coding: utf-8 -*-

import unittest
import datetime
from twopy.thread import make_dat_url, make_thread_url, \
                         make_title_from_dat, parse_dat


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

    def test_make_title_from_dat(self):
        with open("tests/1335621929.dat", "r") as fp:
            dat_string = unicode(fp.read(), "Shift_JIS", "replace")
            title = make_title_from_dat(dat_string)
            self.assertEqual(title, u"【海外】日本向けコメ増産/アメリカ")

    def test_parse_dat(self):
        with open("tests/1335621929.dat", "r") as fp:
            dat_string = unicode(fp.read(), "Shift_JIS", "replace")
            result = parse_dat(dat_string)
            self.assertEqual(len(result["comments"]), 146)
            self.assertEqual(
                result["title"], u"【海外】日本向けコメ増産/アメリカ")
            self.assertTrue(
                isinstance(result["last_retrieved"], datetime.datetime))
