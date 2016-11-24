#!/usr/bin/python
# -*- coding: utf-8 -*-
#def eachFile(filepath):
#    pathDir =  os.listdir(filepath)
#    for allDir in pathDir:
#        child = os.path.join('%s%s' % (filepath, allDir))
#        print child.decode('gbk') # .decode('gbk')是解决中文显示乱码问题
#
#def readFile(filename):
#    fopen = open(filename, 'r') # r 代表read
#    for eachLine in fopen:
#        print "读取到得内容如下：",eachLine
#    fopen.close()
#
#

#import urllib2  
#import urllib  
#import os  
#import shutil  
#  
##homedir = os.getcwd()  
#homedir = "/home/sysop/tmp"
#  
#import os  
#def walk_dir(homedir,fileinfo):  
#    for root, dirs, files in os.walk(homedir):  
#        for name in files:  
#            print(os.path.join(name))  
#            fileinfo.write(os.path.join(root,name) + '\n')  
#        for name in dirs:  
#            print(os.path.join(name))  
#            fileinfo.write('  ' + os.path.join(root,name) + '\n')  
#fileinfo = open(homedir+'/list.txt','w')  
#walk_dir(homedir,fileinfo)  
#
f = open('/home/sysop/tmp/list.txt', 'r')
lists = f.readlines()
for i in lists:
	print i
	
