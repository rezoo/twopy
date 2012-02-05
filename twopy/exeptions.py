#!/usr/bin/env python
# -*- coding: utf-8 -*-


class HttpStatusError(Exception):
    def __init__(self, message, response):
        self.message = message
        self.response = response

    def __str__(self):
        return repr(self.message)


class RegexError(Exception):
    def __init__(self, message, regex):
        self.message = message
        self.regex = regex

    def __str__(self):
        return repr(self.message)


class DatoutError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)


class BrokenThreadError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)
