#!/usr/bin/python
import rrdtool
import time
cur_time=str(int(time.time()))
rrd=rrdtool.create('Flow.rrd','--step','300','--start',cure_time,'DS:eth0_in:COUNTER:600:0:U','DS:eth0_out:COUNTER:600:0:U')
