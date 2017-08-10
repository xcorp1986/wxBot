#!/usr/bin/env python
# coding: utf-8
#

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime


def my_job():
    print 'task running at %s' % datetime.now()
    job = sched.get_job("my_task")
    hour = datetime.now().hour
    if 9 <= hour <= 23:
        if str(job.trigger) != str(CronTrigger(minute='*/1', second='00')):
            sched.reschedule_job(job.id, trigger='cron', minute='*/1', second='00')


if __name__ == '__main__':
    print 'Program Starting @time:%s' % datetime.now()
    sched = BlockingScheduler()
    hour = datetime.now().hour
    if 9 <= hour <= 23:
        sched.add_job(my_job,'cron',minute='*/1', second='00', id='my_task')
    sched.start()

