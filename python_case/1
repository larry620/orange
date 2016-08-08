#!/usr/bin/python
import rrdtool
import time

title="Server network traffic flow ("+time.strftime('%Y-%m-%d',time.localtime(time.time()))+")"
rrdtool.graph( "Flow.png", "--start", "-ld", "--vertical-label=Bytes/s", "--x-grid", "MINUTE:12:HOUR:1:HOUR:1:0:%H")
