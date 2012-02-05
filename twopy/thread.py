#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import StringIO
import gzip
from user import make_anonymous_user
from comment import Comment
from exeptions import HttpStatusError, RegexError


def thread_generator(dat_string):
    for column in dat_string.split("\n"):
        if len(column) == 0:
            return
        result = column.split("<>")
        yield (result[0], result[1], result[2], result[3])


def make_title_from_dat(dat_string):
    tmp_expressions = re.compile(r"^(?P<column>.+?)\n")
    result = tmp_expressions.search(dat_string)
    if result:
        column = result.group("column")
        return column.split("<>")[4]
    else:
        message = "Regex unmathed in parsing the title of the thread."
        raise RegexError(message, tmp_expressions)


def make_thread_url(board_url, dat_name):
    board_expressions = re.compile(r"^(http://.+?)/(\w+)")
    result = board_expressions.search(board_url)
    if result:
        return result.group(1) + "/test/read.cgi/" + \
            result.group(2) + "/" + dat_name[:-4] + "/"
    else:
        message = "Regex unmathed in parsing the board's url: " + board_url
        raise RegexError(message, board_expressions)


def make_dat_url(board_url, dat_name):
    board_url_fixed = \
        board_url if board_url.endswith("/") else board_url + "/"
    return board_url_fixed + "dat/" + dat_name


def retrieve_thread(board_url, dat_name, user=None):
    my_user = user if user else make_anonymous_user()
    target_url = make_dat_url(board_url, dat_name)
    response = my_user.urlopen(target_url, gzip=True)

    if response.code == 200:
        zipped_IO = StringIO.StringIO(response.read())
        unzipped_string = gzip.GzipFile(fileobj=zipped_IO).read()
        dat_string = unicode(unzipped_string, "Shift_JIS", "replace")
        result = []
        for column in dat_string.split("\n"):
            if column == "":
                continue
            result.append(Comment(column))
        return result
    else:
        message = "HTTP status is invalid: " + str(response.code)
        raise HttpStatusError(message, response)
