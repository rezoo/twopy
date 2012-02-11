#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def _response(scanner, token):  return ("RES", token)
def _url(scanner, token):       return ("URL", token)
def _enter(scanner, token):     return ("ENT", token)
def _character(scanner, token): return token


class CommentParser(re.Scanner):
    def __init__(self):
        re.Scanner.__init__(self, [
            (r">>[0-9]{1,4}(-[0-9]{1,4}|)", _response),
            (u"＞＞[０-９]{1,4}(ー[０-９]{1,4}|)", _response),
            (r"(https?|ttp)(:\/\/[-_.!~*\'()a-zA-Z0-9;\/?:\@&=+\$,%#]+)", _url),
            (r"\n", _enter),
            (r".+?", _character),
        ])

    def parse_comment(self, comment_string):
        tokens, remainder = self.scan(comment_string)
        result = []
        word = ""
        for token in tokens:
            if type(token) is unicode:
                word += token
                continue
            if word != "":
                result.append(word)
                word = ""

            if token[0] == "ENT":
                result.append(token[1])
            elif token[0] == "URL":
                result.append(token[1])
            elif token[0] == "RES":
                result.append(token[1])
        return result
