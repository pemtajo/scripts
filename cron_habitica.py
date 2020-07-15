#!/usr/bin/python3
# coding=UTF-8
# encoding=UTF-8
from crontab import CronTab


with CronTab(user="pedro") as cron:
    # cron.remove_all()
    for job in cron:
        print(job)

    # job = cron.new(command="/home/pedro/dev/p/scripts/ajust_habitica_tags.py")
    # job.minute.every(5)
