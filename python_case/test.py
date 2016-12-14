#!/usr/bin/python
# -*- coding: utf-8 -*-



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

#########if not判断##########
#lis= [1, 2, 3]
#guess = int(input('please input: '))
#if guess in lis:
#	print 'if end'
#
#if guess not in lis:
#	print 'not in'
#
#if not guess:
#	print 'null end'
#
#else:
#	print 'else end'
###################

########计算类中函数长度##############
#class MyObject(object):
#	def __init__(self):
#		self.x = 9
#	
#	def power(self):
#		return self.x * self.x
#
#
#obj = MyObject()
#obj1 = obj.power()
##print len('%d'%obj1)
##print len(str(obj1))
#print obj.x
#print MyObject.x
####################

#####################

#class Student(object):
#
#	def get_score(self):
#		return self._score
#
#	def set_score(self, value):
#		if not isinstance(value, int):
#			raise ValueError('hahahaha')
#			raise ValueError('hehehehe')
#		self._score = value
#

#from types import MethodType
#s = Student()
#s.set_score(456)
#print s.get_score()
#		return age
#s.name = 'larry'
#print(s.name)

#def set_age(self, age):
#	self.age = age

#s.set_age = MethodType(set_age, s)
#s.set_age(26)
#print(s.age)


#class Chain(object):
#
#    def __init__(self, path=''):
#        self._path = path
#
#    def __getattr__(self, path):
#        return Chain('%s/%s' % (self._path, path))
#
#    def __str__(self):
#        return self._path
#
#    __repr__ = __str__
#

#print Chain().status.user.timeline.list

#class Student(object):
#
#    def __init__(self):
#        self.name = 'Michael'
#
#    def __getattr__(self, attr):
#		if attr=='score':
#			return 99

#print Student().score
#s = Student()
#print s.name
#print s.score


#import os
#import time
#
#source = ['/home/sysop/tmp/123', '/home/sysop/tmp/234']
#target_dir = '/home/sysop/backup/'
##target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'
#today = target_dir + time.strftime('%Y%m%d')
#now = time.strftime('%H%M%S')
#
#comment = raw_input('enter a comment --> ')
#if len(comment) == 0:
#	target = today + os.sep + now + '.zip'
#else:
#	target = today + os.sep + now + comment.replace(' ', '_') + '.zip'
#
#print target
#
#if not os.path.exists(today):
#	os.mkdir(today)
#	print 'successfully created directory', today
##target = today + os.sep + now + '.zip'
#
#zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))
#tar_command = "tar zcvf %s %s " % (target, ' '.join(source))
#
#print tar_command
#print zip_command
##run the backup
##if os.system(zip_command) == 0:
##	print 'successful backup to', target
##else:
##	print 'backup failed'
##

#{{{#####calss ver and projcet var#####
#class Person:
#	'''represents a person.'''
#	population = 0
#	
#	def __init__(self, name):
#		'''initializes the person's data'''
#		self.name = name
#		print '(initializing %s)' % self.name
#		Person.population += 1
#	
#	def __del__(self):
#		'''i am dying'''
#		print '%s says bye.' % self.name
#		Person.population -= 1
#
#		if Person.population == 0:
#			print 'i am the last one'
#		else:
#			print 'there are still %d people left.' % Person.population
#
#	def sayHi(self):
#		'''greeting by the person,really, that's all it does.'''
#		print 'hi, my name is %s' % self.name
#
#	def howMany(self):
#		'''prints the current population'''
#		if Person.population == 1:
#			print 'i am the only person here'
#		else:
#			print 'we have %d persons here' % Person.population
#
#swaroop = Person('Swaroop')
#swaroop.sayHi()
#swaroop.howMany()
#print " "
#
#kalam = Person('Abdul Kalam')
#kalam.sayHi()
#kalam.howMany()
#print " "
#
#swaroop.sayHi()
#print " "
#swaroop.howMany()
#print " "
#}}}

#{{{#####inherit#####
#class SchoolMember:
#    '''Represents any school member.'''
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
#        print '(Initialized SchoolMember: %s)' % self.name
#
#    def tell(self):
#        '''Tell my details.'''
#        print 'Name:"%s" Age:"%s"' % (self.name, self.age),
#
#class Teacher(SchoolMember):
#    '''Represents a teacher.'''
#    def __init__(self, name, age, salary):
#        SchoolMember.__init__(self, name, age)
#        self.salary = salary
#        print '(Initialized Teacher: %s)' % self.name
#
#    def tell(self):
#        SchoolMember.tell(self)
#        print 'Salary: "%d"' % self.salary
#
#class Student(SchoolMember):
#    '''Represents a student.'''
#    def __init__(self, name, age, marks):
#        SchoolMember.__init__(self, name, age)
#        self.marks = marks
#        print '(Initialized Student: %s)' % self.name
#
#    def tell(self):
#        SchoolMember.tell(self)
#        print 'Marks: "%d"' % self.marks
#
#t = Teacher('Mrs. Shrividya', 40, 30000)
#s = Student('Swaroop', 22, 75)
#
#print # prints a blank line
#
#members = [t, s]
#for member in members:
#    member.tell() # works for both Teachers and Students
#
##}}}

#{{{##### input/ouput#####


#poem ='''\
#programming is fun
#when the work is done
#if you wanna make your work also fun:
#use python!
#'''
#f = file('poem.txt', 'w')
#f.write(poem)
#f.close
#
#f = file('poem.txt')
#
#while True:
#	line = f.readline()
#	if len(line) == 0:
#		break
#	print line,
#f.close()
#


#}}}

#{{{#####storage#####
#!/usr/bin/python
#Filename:pickling.py

#import cPickle as p
#shoplistfile = 'shoplist.data'
#shoplist = ['apple', 'mango', 'carrot']
#
#f = file(shoplistfile, 'w')
#p.dump(shoplist, f)
#f.close()
#
#del shoplist
#
#f = file(shoplistfile)
#storedlist = p.load()
#print storedlist
#

#}}}

#{{{#####try..except#####
#!/usr/bin/python
#Filename: try_except.py

#import sys
#
#try:
#	s = raw_input('enter something --> ')
#	#s = int(raw_input('enter something --> '))
#except EOFError:
#	print '\nWhy did you do an EOF on me?'
#	sys.exit()
#except:
#	print '\nSome error/exception occurred'
#
#print 'Done'
#

#}}}

#{{{#####raising#####
#class ShortInputException(Exception):
#    '''A user-defined exception class.'''
#    def __init__(self, length, atleast):
#        Exception.__init__(self)
#        self.length = length
#        self.atleast = atleast
#
#try:
#    s = raw_input('Enter something --> ')
#    if len(s) < 3:
#        raise ShortInputException(len(s), 3)
#    # Other work can continue as usual here
#except EOFError:
#    print '\nWhy did you do an EOF on me?'
#except ShortInputException, x:
#    print 'ShortInputException: The input was of length %d, \
#          was expecting at least %d' % (x.length, x.atleast)
#else:
#    print 'No exception was raised.'
#



#}}}

#{{{#####try...except#####
#try:
#    print  aa
#except  NameError, msg:
#    print  msg
# }}}

#{{{#####raise#####
#filename = raw_input('please input file name:')
#if filename == 'hahaha':
#	raise a('input file name error !')
#}}}

#{{{#####try...finally#####
#import time
#
#try:
#    f = file('poem.txt')
#    while True: # our usual file-reading idiom
#        line = f.readline()
#        if len(line) == 0:
#            break
#        time.sleep(2)
#        print line,
#
#finally:
#    f.close()
#    print 'Cleaning up...closed the file'
#
##}}}

#{{{#####sys_module#####
#!/usr/bin/python
# Filename: cat.py

#import sys
#
#def readfile(filename):
#    '''Print a file to the standard output.'''
#    f = file(filename)
#    while True:
#        line = f.readline()
#        if len(line) == 0:
#            break
#        print line, # notice comma
#    f.close()
#
## Script starts from here
#if len(sys.argv) < 2:
#    print 'No action specified.'
#    sys.exit()
#
#
#if sys.argv[1].startswith('--'):
#    option = sys.argv[1][2:]
#    # fetch sys.argv[1] but without the first two characters
#    if option == 'version':
#        print 'Version 1.2'
#    elif option == 'help':
#        print '''\
#This program prints files to the standard output.
#Any number of files can be specified.
#Options include:
#  --version : Prints the version number
#  --help    : Display this help'''
#    else:
#        print 'Unknown option.'
#    sys.exit()
#else:
#    for filename in sys.argv[1:]:
#        readfile(filename)
#
#
#
##}}}

#{{{#####powersum*args#####

#def powersum(power, *args):
#	total = 0
#	for i in args:
#		total += pow(i, power)
#	return total
#print powersum(2, 3)
#


#}}}

#{{{#####lambda#####
#!/usr/bin/python
#Filename: lambda.py

#def make_repeater(n):
#	return lambda s: s*n
#twice = make_repeater(2)
#
#
#print twice('word')
#print twice(5)
#




#}}}

#{{{conc
#import os
#import sys
#
#class test:
#	def __init__(self, name, number):
#		self.name = name
#		self.number = number
#	def  sayhi(self):
#		print '(your name is %s, number is %s)' % (self.name, self.number)
#
#
#
#conc_list={'boy':'11', 'girl':'12', 'gay':'13'}
#avg1 = sys.argv[1]
#
##t.sayhi()
#def show_con():
#	for a, b in conc_list.items():
#		t = test(a, b)
#		t.sayhi()
#
#def add_con():
#	#try:
#	avg2 = sys.argv[2]
#	if len(sys.argv) != 3:
#	#except:
#		print "error"
#	else:
#		conc_list['avg1'] = avg2
#
#	
#
#def del_con():
#	avg1 = sys.argv[1]
#	if len(sys.argv) != 2:
#		print "error"
#	else:
#		del conc_list['avg1']
#
#
##show_con()
#del_con()
#show_con()
##}}}

##{{{#####conc_ex#####
#import cPickle as p  
#  
#class person:    
#    ''''' defined class person'''     
#    def getname(self):  
#        return self.name   
#    def setname(self,name):  
#        self.name = name  
#    def getad(self):  
#        return self.address   
#    def setad(self,address):  
#        self.address = address        
#          
#
#dic ={}  
#
#def addp(cname,name,adress):     
#    t=person()  
#    t.setname(name)  
#    t.setad(adress)  
#    dic[name]=t  
#
#def delp(name):  
#	print dic[name]
#    #del dic[name]  
#  
#      
#def write():  
#    f = file("dic.data",'w')  
#    p.dump(dic,f)  
#    f.close()      
#
#def read():  
#    f=file("dic.data")  
#    dic = p.load(f)  
#         
#def search(name):  
#    '''''search person'''  
#    read()  
#    p = person()  
#    if name in dic:  
#        p=dic[name]  
#        print "%s de adress is %s"%(name,p.getad())  
#    else:  
#        print"%s cannot find"%(name)  
#  
#def view():  
#    ''''' view all person  information'''  
#    f=file("dic.data")  
#    dic = p.load(f)  
#    for name,cname in dic.items():  
#            print '%s in %s at %s' % (cname,name, dic[name].getad())  
#
#dic
#  
#while True:  
#    s= raw_input("enter cmd-->\n")  
#    if(s=="quit"):  
#        break  
#    else:  
#        exec s  
#
##}}}

##{{{#####spider_urllib#####
#import urllib

#f = urllib.urlopen('http://glpi.larry.com/')
#f = urllib.quote('http://glpi.larry.com/')
#one = f.geturl()
#print f
#for i in one:
#	print i

#}}}

#{{{#####slot
#from tmodule.test_module import *


#class Student:
#	pass
#
#s = Student()
#s.set_age = MethodType(set_age, s) 
#s.name = 'larry'
#s.set_age(25)
#s.age
##print (s.name)
##print (s.set_age)

#}}}

#{{{#####装饰器property用法#####
#class screen():
#
#    @property
#    def width(self):
#        return self.width
#
#    @width.setter
#    def width(self, value):
#        if not isinstance(value, int):
#            raise ValueError('width must be an int')
##       if value < 0 or value >1024:
#        if value != 1024:
#            raise ValueError('width muset between 0~1024')
#        self.width = value
#
#
#    @property
#    def height(self):
#        return self.width
#
#    @height.setter
#    def height(self, value):
#        self.height = value
#
#
#    @property
#    def resolution(self):
#        return  self.width * self.height
#
#
#s = screen()
#s.width = 9.9
#s.height = 768
##print s.width
##print s.height
#
#

##}}}

#{{{#####map#####
#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回, map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list

#def f(x):
#...     return x * x
#...

#>>> r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
#>>> list(r)
#[1, 4, 9, 16, 25, 36, 49, 64, 81]

#


#}}}

#{{{#####lambda#####
#lambda表达式是起到一个函数速写的作用。允许在代码内嵌入一个函数的定义。
#阶乘
#n = 5
#reduce(lambda x,y:x*y, range(1,n+1))
#120

#加法
#f = lambda x,y,z:x+y+z
#f = (1, 2, 3)
#6


#}}}

#{{{ #####importmodule and if__name__ us
#每个Python模块都有它的__name__，如果它是'__main__'，这说明这个模块被用户单独运行，我们可以进行相应的恰当操作
#!/usr/bin/python
# Filename: tmp.py

#def sayhi():
#    print 'Hi, this is mymodule speaking.'
#
#version = '0.1'
#
#if __name__ == '__main__':
#    print 'This program is being run by itself'
#else:
#    print 'I am being imported from another module'
#
##!/usr/bin/python
## Filename: tmp1.py
#
#import tmp
#tmp.sayhi()
#print 'Version', tmp.version
#
#}}}

#{{{#####列表表达式#####
#L1 = ['Hello', 'World', 18, 'Apple', None]
##L2=[]
##for i in L1:
##   if isinstance(i, str) == True:
##       L2.append(i.lower())    
#L2 = [i.lower() for i in L1 if isinstance(i, str)]
#}}}

#{{{#####生成器#####
#如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。要把一个列表生成式的[]改成()，就创建了一个generator：,函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行

#g = (x * x for x in range(10))
#for i in g:
#	print (i)


#杨辉三角



#}}}

#{{{#####yield#####


#}}}

#{{{#####filter#####
#filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
#在一个list中，删掉偶数，只保留奇数
#def is_odd(n):
#	return n % 2 == 1

#print filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])


#}}}



