# -*- coding: utf-8 -*-

import os
import unittest
from twopy.board import make_subject_url, parse_board


class TestBoardModule(unittest.TestCase):
    def test_subject_url(self):
        result = make_subject_url("http://engawa.2ch.net/news/")
        self.assertEqual(result, "http://engawa.2ch.net/news/subject.txt")
        result = make_subject_url("http://engawa.2ch.net/news")
        self.assertEqual(result, "http://engawa.2ch.net/news/subject.txt")

    def test_parse_board(self):
        filepath = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "data", "subject.txt")
        with file(filepath, "r") as fp:
            text = unicode(fp.read(), "Shift-JIS", "ignore")
            result = parse_board(text)
            self.assertEqual(type(result), list)
            self.assertEqual(type(result[0]), dict)
            self.assertEqual(len(result), 378)

            self.assertEqual(result[0]["dat"], u"1328886973.dat")
            self.assertEqual(result[0]["res"], 33)
            self.assertEqual(result[0]["title"],
                u"【ﾋｬｯﾊｰ】 NATO軍、タリバンと間違えうっかり子供8人をぶち殺す")
            self.assertEqual(result[9]["dat"], u"9241201701.dat")
            self.assertEqual(result[9]["res"], 10)
            self.assertEqual(result[9]["title"],
                u"ステマと言われて困っています。- ２ちゃんねる知恵袋")
