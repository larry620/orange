import os
total = float(77370)
list =open('/home/sysop/conf/tt.list', 'r')

for i in list:
    cl1=i.strip()
    cl2=cl1.split()
    if cl2[:1]:
	res=cl2[:1][0]
	res2=cl2[-1]
        


    #print c1
        #print "%s \t %s \t  %.2f%%" % (res,res2,(float(res)/total*100))
        #print res,"\t%.2f%%" %(float(res)/total*100),res2
    #print "%%"
