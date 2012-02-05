#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from user import make_anonymous_user
from exeptions import HttpStatusError, RegexError


def parse_2ch_boards(string):
    board_expression = re.compile(
        r"<A HREF=(?P<url>http://\w+\.2ch\.net/\w+\/)>(?P<title>.+?)</A>")
    category_expression = re.compile(
        r"<BR><BR><B>(?P<title>.+?)</B><BR>")

    result = []
    for string in string.split("\n"):
        category_result = category_expression.search(string)
        if category_result:
            result.append({
                "category": category_result.group("title"),
                "boards": []})
            continue
        board_result = board_expression.search(string)
        if board_result and len(result) > 0:
            result[-1]["boards"].append({
                "title": board_result.group("title"),
                "url": board_result.group("url")})
    return result


def retrieve_2ch_boards(url="http://menu.2ch.net/bbsmenu.html", user=None):
    my_user = user if user else make_anonymous_user()

    response = my_user.urlopen(url, gzip=False)
    if response.code == 200:
        html_string = unicode(response.read(), "Shift_JIS", "ignore")
        return parse_2ch_boards(html_string)
    else:
        message = "HTTP status is invalid: %i" + str(response.code)
        raise HttpStatusError(message, response)
