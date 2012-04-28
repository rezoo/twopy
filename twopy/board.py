#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from user import make_anonymous_user
from exeptions import HttpStatusError, RegexError


def make_subject_url(url):
    if url.endswith("/"):
        return url + "subject.txt"
    else:
        return url + "/subject.txt"


def parse_board(string):
    if not isinstance(string, unicode):
        raise TypeError("unsupported string type:" + str(type(string)))
    thread_expressions = re.compile(
        r"^(?P<dat>\d+\.dat)<>(?P<title>.*) \((?P<n_comments>\d*)\)$")
    results = []
    for thread_string in string.split("\n"):
        thread_data = thread_expressions.search(thread_string)
        if thread_data:
            results.append({
                "title": thread_data.group("title"),
                "n_comments": int(thread_data.group("n_comments")),
                "dat": thread_data.group("dat"),
            })
        elif len(thread_string) != 0:
            raise RegexError(
                "Regex unmatched in parsing the thread's data",
                thread_expressions)
    return results


def retrieve_board(board_url, user=None):
    my_user = user if user else make_anonymous_user()
    subject_url = make_subject_url(board_url)

    response = my_user.urlopen(subject_url, gzip=False)
    if response.code == 200:
        retrieved_string = unicode(response.read(), "Shift_JIS", "ignore")
        print type(retrieved_string)
        return parse_board(retrieved_string)
    else:
        message = "HTTP status is invalid: " + str(response.code)
        raise HttpStatusError(message, response)
