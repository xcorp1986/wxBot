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
                self.send_msg(u'可爱的人儿就是我', u'OK~~~%s' %datetime.now())

        time.sleep(10)


def main():
    bot = MyWXBot()
    bot.DEBUG = True
    # bot.conf['qr'] = 'png'
    bot.run()


if __name__ == '__main__':
    print 'Program Starting @time:%s' % datetime.now()
    main()