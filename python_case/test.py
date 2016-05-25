
#import re
#f = open('name.txt' , 'r')
#for line in f:
#    line = line.strip()
#    pattern = 'c.c'
#    result = re.search(pattern, line)
#    if result:
#	print 'name is {0}'.format(line)
#	#print line
#f.close()


#words = ['pear', ' ', 'apple', 'orange', 'ghaha', ' ']
#lst = []
#for word in words:
#	if not word.strip():
#		#continue
#		break
#else:
#	print word
#for i in random.randint(1,2): 
#for i in randint(1,2): 
#for i in random(1,2): 
#	print i

#from random import randint
#def odd (n):
#	return n % 2
#
#allNums = []
#for eachNum in range (9):
#	allNums.append (randint (1, 99))
#print filter (odd, allNums)
#d = {'x': 1, 'y': 2, 'z': 3}
#for key in d:
#    print key, 'correspondsto', d[key]
#for key, value in d.items(): 
#    print key, 'corresponds to', value


#d = [1, 2, 3, 4, 5]
#z = ['a', 'b', 'c', 'd', 'e', 'fg']
#index = 0
#for string in z:
#    if 'b' in string:
#        z[index] = '[haha]'
#    index +=1
#    print z

#from math import sqrt
#for n in range(16, 0, -1):
#    root = sqrt(n)
#    if root == int(root):
#        print n
#        break

#result = []
#for x in range(3):
#    for y in range(3):
#        result.append((x, y))
#print result
#
#def hello(name):
#    return'hello, ' + name + '!'
   # print hello('man')
#    return 'hello' + n
#try_to_change('larry')  
#print hello('boy')
#storage = {}
#storage['first'] = {}
#storage['middle'] = {}
#storage['last'] = {}
#me = 'a b c'
#storage['first']['a'] = me
#storage['first']['a'] = me
#storage['middle']['b'] = me
#print storage
#print storage['first']

#def init(data):
#    data['first'] = {}
#    data['middle'] = {}
#    data['last'] = {}
#storage = {}
#init (storage)

#def lookup(data, label, name):
#    print data[label].get(name)
#
##

##class parent(object):
##    def parentmethod(self):
##        print 'calling parent method'
##
##class child(parent):
##    def childmethod(self):
##        print 'calling child method'
##
##p = parent()
##p.parentmethod()
##
#class P(object):
#    def foo(self):
#        print 'hi, i am P-foo()'
#
#class C(P):
#    def foo(self):
#        print 'hi, i am C-foo()'
#p = P()
#p.foo()

#c = C()
#c.foo()

#P.foo(c)

#class RoundFloat(float):
#    def __new__ (cls, val):
#        print val 
#        print super(RoundFloat, cls)
#        return super(RoundFloat, cls). __new__ (cls, round(val, 2))
#aa=RoundFloat(1.63545)
#print type(aa)
#
##print RoundFloat. __bases__

#class Time60(object):
#    def __init__ (self, hr, min):
#        self.hr = hr
#        self.min = min
#
#    def __str__ (self):
#        return '%d:%d' % (self.hr, self.min)
#
#mon = Time60(10, 30)
#tue = Time60(11, 15)
#
#print mon, tue

#    def hello(self):
#        print 'hi %s ' % max
#        print 'hi %s ' % self.hr
#
#aaa=Time60(10, 1)
#print aaa
##aaa.hello()

#class Student(object):
#    def __init__(self, name):
#        self.name = name
#    def __str__(self):
#        return 'Student object (name: %s)' % self.name
#
#    def testa(self):
#        print self.name.lower()
#       # print self.name
#        
#        
#
#stud = Student('LARrY')
#stud.testa()
#print stud
#
#class Fib(object):
#    def __getitem__(self, n):
#        if isinstance(n, int):
#            a = 1
#            b = 1
#            for x in range(n):
#                a = b
#                b = a + b
#            return a
#
#        if isinstance(n, slice):
#            start = n.start
#            stop = n.stop
#            print start
#            print stop
#            if start is None:
#                start = 0
#            a = 1
#            b = 1
#            L = []
#            for x in range(stop):
#                if x >= start:
#                    L.append(a)
#                a = b
#                b = a + b
#            return L
#
#
#testaa = Fib()
#print testaa[0:5]

#def hour_ahead(offseta):
#    offsetb = int(offseta)
#    print offsetb
#    #dt = datetime.datetime.now() + datetime.timedelta(hours=offsetb)
#    dt = 'a'
#    html = "<html><body>In %s hour(s), it will be %s.</html></body>" % (offseta, dt)
#    print offseta
#    print html
##    return HttpResponse(html)
#hour_ahead(5)

#list1 = []
#list = [['a', 'b', 'c'],['1', '2', '3']]
##list1 = [[list[0][1]],[list[1][1]]]
#for i in list:
##	print i
##	plist = list1.append(i[1].split())
#	plist = list1.append(i[1])
##	print plist
#print list1
#


#mylist = [[['a','b','c'],['d','f','g']],[['h','i','j'],['k','l','m']]];
#print mylist[0]
#res = [mylist[i][j][1] for i in range(len(mylist)) for j in range(len(mylist[i]))];
#for i in range(len(mylist)): 
#	print "i =", i
#	for j in range(len(mylist[i])):
#		print "j =", j
#
#res = [mylist[i][j][1]]
#print (res)
lis= [1, 2, 3]

guess = int(input('please input: '))

if guess in lis:
	print 'if end'

if guess not in lis:
	print 'not in'

if not guess:
	print 'null end'

else:
	print 'else end'



















