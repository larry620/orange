li = []
def getPid(process):
	import commands
	import sys
	import os
#	import logging
	cmd = "ps aux | grep -v grep |grep '%s' " % process
	info = commands.getoutput(cmd)
	txt = info.readlines()
	print txt
	infos = info.split('\n')
	for i in infos:
		j = i.split()
		li.append(j[1])

getPid('nginx')
#for i in li:
#    print i
