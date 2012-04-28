#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import StringIO
import gzip
import datetime
from user import make_anonymous_user
from comment import Comment
from exeptions import HttpStatusError, RegexError


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
        return Thread(dat_string)
    else:
        message = "HTTP status is invalid: " + str(response.code)
        raise HttpStatusError(message, response)


class Thread:
    def __init__(self, dat_string):
        self._title = make_title_from_dat(dat_string)
        self._comments = []
        for column in dat_string.split("\n"):
            if column == "":
                continue
            self._comments.append(Comment(column)) 

    def get_title(self):
        return self._title
    title = property(get_title)

    def get_comments(self):
        return self._comments
    comments = property(get_comments)

    def __len__(self):
        return len(self._comments)

    def __iter__(self):
        for comment in self._comments:
            yield comment
    
    def __getitem__(self, key):
        if type(key) is int:
            return self._comments[key - 1]
        elif type(key) is slice:
            return self._comments[slice(key.start - 1, key.stop, key.step)]
        else:
            raise TypeError("The type %s is not supported." % repr(type(key)))
