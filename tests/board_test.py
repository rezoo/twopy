# -*- coding: utf-8 -*-

import unittest
from twopy.board import make_subject_url, parse_board


class TestBoardModule(unittest.TestCase):
    def test_make_subject_url(self):
        self.assertEqual(
            make_subject_url("http://engawa.2ch.net/news/"),
            "http://engawa.2ch.net/news/subject.txt")
        self.assertEqual(
            make_subject_url("http://engawa.2ch.net/news"),
            "http://engawa.2ch.net/news/subject.txt")

    def test_parse_board(self):
        with open("tests/subject.txt", "r") as fp:
            retrieved_string = unicode(fp.read(), "Shift_JIS", "ignore")
            result = parse_board(retrieved_string)

            self.assertEqual(len(result), 498)
            self.assertEqual(
                result[0]["title"],
                u"【北海道】迫力満点ヒグマに児童興奮　サホロリゾートのベア・マウンテンが２８日に今季オープン")
            self.assertEqual(result[0]["res"], 62)
            self.assertEqual(result[0]["dat"], "1335616215.dat")
            self.assertEqual(
                result[-1]["title"],
                u"【社会】「死んで償ってもらう」死亡妊婦の夫★１０")
            self.assertEqual(result[-1]["res"], 1001)
            self.assertEqual(result[-1]["dat"], "1335258095.dat")
