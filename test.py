#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from twopy.board import retrieve_board
from twopy.thread import retrieve_thread
from twopy.utility import retrieve_2ch_boards

def main():
    board_url = "http://uni.2ch.net/newsplus/"
    result = retrieve_board(board_url)
    print result[0]["title"], result[0]["res"], result[0]["dat"]
    retrieve_thread(board_url, result[0]["dat"])
    """
    result = retrieve_2ch_boards()
    for category in result:
        print category["category"]
        for board in category["boards"]:
            print "    ", board["title"], board["url"]

    return 0
    """


if __name__ == "__main__":
    sys.exit(main())
