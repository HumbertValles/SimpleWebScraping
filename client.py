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
import telebot
import sys


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

    def print_title(self, bookTitle):
        """
        If the arguments Bot Token and chat_id were received through
        the command line, a message is sent to that chat. Otherwise,
        it only shows the name of the book on the screen
        """

        if len(sys.argv) == 3:
            beepBoop = telebot.TeleBot(sys.argv[1])  #token
            beepBoop.send_message(sys.argv[2], "Today's free ebook is: "
                                + bookTitle)  #chat_id
            print "Message sent to your chat"
        else:
            print "Today's free ebook is: "+bookTitle

    def run(self):
        """
        Retrieves the title of the free daily book and prints it
        """

        html = self.get_web_page(
                "https://www.packtpub.com/packt/offers/free-learning/")
        bookTitle = self.get_title(html)
        print bookTitle
        self.print_title(bookTitle)


if __name__ == "__main__":

    client = Client()
    client.run()
