#!/usr/bin/env python
# coding: utf-8
#

from datetime import datetime
from wxbot import *


class MyWXBot(WXBot):
    def schedule(self):
        hour = datetime.now().hour
        minute = datetime.now().minute
        if 9 <= hour <= 23:
            if minute % 10 == 0:
                self.send_msg(u'歡樂今宵', u'OK~~~%s' % datetime.now())

        time.sleep(61)


def main():
    bot = MyWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'tty'
    bot.run()


if __name__ == '__main__':
    print 'Program Starting @time:%s' % datetime.now()
    main()