#!/usr/bin/python
#coding:utf8
import threading
import time
import os
import shutil
import re
fuhao=os.linesep
start_time=int(time.strftime('%H%M%S'))
print start_time

def count_cpu_heshu():
    file=open('/proc/cpuinfo')
    cpu_sum=[]
    
    for line in file.readlines():
        cpu_he=re.findall('^processor', line)
        if len(cpu_he)==1:
            cpu_sum.append(cpu_he)
        else:
            continue
    file.close()
    return len(cpu_sum)
    print len(cpu_sum)
#s=count_cpu_heshu()
#print(s)
