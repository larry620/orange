import commands
import sys
import os
import linecache

li = []

def getPid(process):
	cmd = "ps aux | grep -v grep |grep '%s' " % process
	info = commands.getoutput(cmd)
#	txt = info.readlines()
#	print txt
	infos = info.split('\n')
	print "infos =", infos
	aaa = [row[0] for row in info]
	print "aaa =", aaa
	for i in infos:
		print "i =", i
		j = i.split()
			
		print "j =", j
		li.append(j[1])

getPid('nginx')

#if __name__ == '__main__':
#	for b in li:
#		cmd1 = "kill %s" % b
#		end = commands.getoutput(cmd1)
#		print cmd1
#    
