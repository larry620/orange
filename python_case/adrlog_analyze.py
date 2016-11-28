#!/usr/bin/python
#_*_coding:utf-8_*
"""分析线上日志，统计vip 章节id，用户id等 """
import re

f = open('/home/sysop/conf/30_adr.access.log').readlines()
f1 = open('/home/sysop/conf/30_adr.access.log').read()
#f.sort()
#print f
#print f1
#tcount = re.findall(r'7', f1)
#print tcount.group()
cidlist = []

for i in f:
	s = i.split('|')
	cid = s[1]
	print tcount

def_countcid():
	for cid1 in cidlist:
		pass
