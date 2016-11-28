#!/usr/bin/env python
#encoding=utf-8

import datetime,os,sys
import socket


hostname   = socket.gethostname()
today      = datetime.date.today() 
yesterday  = today - datetime.timedelta(days=1)
yesterday  = yesterday.strftime("%Y%m%d")
findFile     = """cd %(local)s;  find . -name "%(find)s"   -exec mv {} %(remote)s{}_%(yesterday)s_%(hostname)s \;"""
#compressFile = """cd %(remote)s; find . -name "*%(yesterday)s_%(hostname)s"  -exec pbzip2 -9 {} \;"""
#accreditFile = """cd %(remote)s; find . -name "*%(yesterday)s_%(hostname)s*" -exec chmod 644 {} \;"""

file = { "nginx" : { "local"  : "/usr/local/nginx/logs/",
                     "find"   : "*.log",
                     "remote" : "/data/logs/",
                     "command": "/etc/init.d/nginx reload"
                   },
       }
 
def main():
    for v1 in file.keys():
        file[v1]["yesterday"] = yesterday
        file[v1]["hostname"]  = hostname
        if os.path.isdir(file[v1]["local"]):
            if not os.path.isdir(file[v1]["remote"]):
                os.makedirs(file[v1]["remote"])
            #print os.popen(findFile %file[v1]).read()
            os.popen(findFile % file[v1]).read()
       #     os.popen(file[v1]["command"])
#      #     print os.popen(compressFile %file[v1]).read()
#      #      os.popen(accreditFile %file[v1])
main()
