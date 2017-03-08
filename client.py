#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Simple web client to get the title of the free daily
book from https://www.packtpub.com, using URLLIB2

@author: HumbertValles
'''

import urllib2
import bs4


class Client(object):

    """Web Client, for https://www.packtpub.com

    Downloads the page
    https://www.packtpub.com/packt/offers/free-learning/
    to find the title of the book
    """

    def __init__(self):
        super(Client, self).__init__()

    def get_web_page(self, url):
        """
        Retrieves an HTML URL returns, HTML
        """
        raise NotImplementedError

    def get_title(self, html):
        """
        Parses the html page searching for the title of the book
        """
        raise NotImplementedError

    def print_title(self, data):
        """
        Prints data retrieved
        """
        raise NotImplementedError

    def run(self):
        """
        Retrieves the title of the free daily book and prints it
        """
        html = self.get_web_page("https://www.packtpub.com/packt/offers/free-learning/")
        bookTitle = self.get_title(html)
        self.print_title(bookTitle)
                

if __name__ == "__main__":
    client = Client()
    client.run()
