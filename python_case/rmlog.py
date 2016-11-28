#!/usr/bin/env python
#_*_coding:utf-8_*_

import os
import sys
import time

class DeleteLog:
    

    def __init__(self, fileName, days):
        self.fileName = fileName
        self.days = days

    def delete(self):
        if os.path.isfile(self.fileName):
            fd = open(self.fileName, 'r')
            while 1:
                buffer = fd.readline()
                if not buffer : break
                if os.path.isfile(buffer):
                    os.remove()
            fd.close()
        elif os.path.isdir(self.fileName):
            for i in [os.sep.join([self.fileName,v]) for v in os.listdir(self.fileName)]:
                #print i
                if os.path.isfile(i):
                    os.remove(i)
                elif os.path.isdir(i):
                    self.fileName = i
                    self.delete()

    def compare_file_time(self,file):
        time_of_last_access = os.path.getatime(file)
        age_in_days = (time.time()-time_of_last_access)/(60*60*24)
        print age_in_days 
        if age_in_days > self.days:
            return True
        return False

if __name__ == '__main__':
    if len(sys.argv) == 2:
        obj = DeleteLog(sys.argv[1],0)
        obj.delete()
    elif len(sys.argv) == 3:
        obj = DeleteLog(sys.argv[1],int(sys.argv[2]))
        obj.delete()
    else:
        print "usage: python %s listfFileName | dirName [days]" % sys.argv[0]
        sys.exit(1)
        
#test1 = DeleteLog('/data/log', 5)
        
