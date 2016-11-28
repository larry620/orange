def getPid(process):
    import commands
    import sys
	import logging
    cmd = "ps aux | grep '%s' " % process
	print cmd
    logging.info(cmd)
    info = commands.getoutput(cmd)
	print info
    infos = info.split()
	print infos
    if len(infos) > 1:
        return infos[1]
    else:
        return -1
print getPid(nginx)
