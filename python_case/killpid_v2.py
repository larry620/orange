import sys,os
pid_list = []
def kill_id(process):
	cmd = "ps aux | grep -v grep|grep -v '''killpid_v2.py''' | grep %s " % process
#	print "cmd1 =", cmd
	f = os.popen(cmd)
	txt = f.readlines()
#	print "txt =" ,txt
	for line in txt[0:]:
		print "line =", line
		colum = line.split()
		pid = colum[1]
		if  'master' not in line:
			print "haha"

		plist = pid_list.append(pid[0:])
	#print pid_list
		

	

process = sys.argv[1]
kill_id(process)


#if __name__ == '__main__':
#
#	if not len(sys.argv)==2:
#		sys.exit()
#
#	for i in pid_list:
#		print i
#		cmd = "kill %d " % int(i)
##		print "cmd2 =", cmd
#		os.system(cmd)
#
