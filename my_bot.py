#!/usr/bin/env python
# coding: utf-8
#

from datetime import datetime
from wxbot import *


class MyWXBot(WXBot):
    def schedule(self):
        self.send_msg(u'欢乐今宵', u'OK~~~%s' %datetime.now())
        time.sleep(600)


def main():
    bot = MyWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()


if __name__ == '__main__':
    print 'Program Starting @time:%s' % datetime.now()
    main()