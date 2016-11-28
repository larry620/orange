#!/usr/bin/python
# -*- coding: utf-8 -*-

#f=open("/home/sysop/conf/adr.access-v2.log_20161122").readline()


for f in open("/home/sysop/conf/adr.access-50.log").readlines():
#	print f
	chid = f.split('|')
	print chid[1]
