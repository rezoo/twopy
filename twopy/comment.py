#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import datetime
from xml.sax.saxutils import unescape
from user import make_anonymous_user
from exeptions import HttpStatusError, RegexError


class Comment:
    __tag_expressions = re.compile(r"<.+?>")
    __date_id_expressions = re.compile(r" ID:")
    __trip_expressions = re.compile(u"◆(?P<trip>\\w+)$")
    __datetime_expressions = re.compile(
        (r"(?P<year>\d{2,4})/(?P<month>\d{2})/(?P<day>\d{2})(\(.*\)|) "
          "(?P<hour>\d{2}):(?P<min>\d{2}):(?P<sec>\d{2})(\.(?P<csec>\d+)|)"))

    def parse_body(self, string):
        return unescape(Comment.__tag_expressions.sub(
            "", string.replace(" <br> ", "\n")))[1:-1]

    def parse_datetime(self, string):
        result = Comment.__datetime_expressions.search(string)
        year = int(result.group("year"))
        month = int(result.group("month"))
        day = int(result.group("day"))
        hour = int(result.group("hour"))
        minute = int(result.group("min"))
        sec = int(result.group("sec"))
        csec = result.group("csec")
        csec_fixed = int(csec) if csec else 0

        return datetime.datetime(
            year, month, day, hour, minute, sec, csec_fixed * 10000)

    def parse_others(self, string):
        result = Comment.__date_id_expressions.search(string)
        if result:
            return (self.parse_datetime(string[:result.start()]),
                    string[result.end():])
        else:
            return (self.parse_datetime(string), "")

    def __init__(self, column_string):
        result = column_string.split("<>")
        self._raw_column = column_string
        self._name = result[0]
        self._email = result[1]
        (self._datetime, self._id) = self.parse_others(result[2])
        self._raw_body = self.parse_body(result[3])

    def get_raw_column(self):
        return self._raw_column
    raw_column = property(get_raw_column)

    def get_email(self):
        return self._email
    email = property(get_email)

    def get_datetime(self):
        return self._datetime
    datetime = property(get_datetime)

    def get_id(self):
        return self._id
    ID = property(get_id)

    def get_raw_body(self):
        return self._raw_body
    raw_body = property(get_raw_body)
