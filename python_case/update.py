#!/usr/bin/python
import rrdtool
import time,psutil
total_input_traffic = psutil.net_io_counter()[1]
total_output_traffic = psutil.net_io_counter()[0]
starttime=int(time.time())
update = rrdtool.updatev('/home/sysop/test/rrdtool/Flow.rrd', '%s:%s:%s' % (str(starttime),str(total_input_traffic),str(total_output_traffic)))
print update
