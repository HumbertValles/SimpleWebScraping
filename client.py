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
    Downloads the page https://www.packtpub.com/packt/offers/free-learning/
    to find the title of the book
    """

    def __init__(self):
        super(Client, self).__init__()

    def get_web_page(self, url):
        """
        Retrieves an HTML URL returns, HTML
        """
        f = urllib2.urlopen(url)
        html = f.read()
        f.close()
        return html

    def get_title(self, html):
        """
        Parses the html page searching for the title of the book
        """

        bs = bs4.BeautifulSoup(html, 'lxml')
        title = bs.find("div", "dotd-title").h2.string.strip()
        return title

    def print_title(self, title):
        """
        Prints data retrieved
        """
        print title

    def run(self):
        """
        Retrieves the title of the free daily book and prints it
        """
        html = self.get_web_page(
                "https://www.packtpub.com/packt/offers/free-learning/")
        bookTitle = self.get_title(html)
        print "Today's free ebook is: "+bookTitle


if __name__ == "__main__":

    client = Client()
    client.run()
