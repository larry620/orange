#!/usr/bin/python
#-*-coding:utf-8-*-

import os
import time
import socket
from datetime import date
from dateutil.relativedelta import relativedelta

number = 86400

def getTime(mothed="before"):
    curdate = time.strftime("%Y-%m-%d")
    if mothed=="before":
        return int(time.mktime(time.strptime(curdate,"%Y-%m-%d")))-number
    else:
        return int(time.mktime(time.strptime(curdate,"%Y-%m-%d")))


def lastDate():
    d = date.today() + relativedelta(days=-1)
    return str(d)


def getFile(fr,fw):
    lock = 0
    for i in fr.readlines():
        if i.startswith("SET timestamp="):
            infiletime = int(i.split("=")[1].replace(';',''))
            if infiletime >= getTime() and infiletime <= getTime(mothed=0):
                lock = 1
            else:
                lock = 0
        #if lock and not i.startswith("#"):
        if lock:
            fw.write(i)
    fw.close()
    fr.close()


if __name__ == '__main__':
    for i in range(2,12):
        fw = open("/software/wangjun/logs/slow_log/slow_%s_33%.2d_%s.log" % (socket.gethostname(),i,lastDate()),"a")
        #fw = open("/root/slow_%s_33%.2d_%s.log" % (socket.gethostname(),i,lastDate()),"a")
        fr = open("/data/mysql/33%.2d/data/slow.log" % i,"r")
        getFile(fr,fw)
