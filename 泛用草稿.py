'''
import numpy as np
a = np.arange(6).reshape(2,3)
for x in np.nditer(a, flags=['external_loop']):
    print(type(x))
    print (x)
'''
'''
if not(0):
    print('0 = false')
else:
    print('0 = true')
'''
'''
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        #return 'hello world'
        return repr((self.name, self.grade, self.age))
a = Student('Bob', 'A', 88)
print(a)
'''
'''
from operator import itemgetter
a = [[1,1],[1,3],[2,3],[2,1]]
b = []
#b.append(a[])
b = repr(lambda a: a[0])
print(b)
'''
'''
c = [  
    '决',  
    '决决',  
    '决决决',  
    '决决决决',  
    '决决决决决',  
    '决决决决决决',  
    '决决决决决决决'  
] 
def chinese(data):
    count = 0
    for s in data:
        if ord(s) > 127:
            count += 1
    return count

print('----通过函数计算长度格式化：----')
for x in range(len(c)):
    number = chinese(c[x])
    newStr = '{0:{wd}}'.format(c[x],wd=20-number)
    print('|%s|' % newStr)
'''
'''
import sys

print('\raaaa','ccc', sep = '|', flush = True)
#sys.stdout.flush()
print('\rbb', flush = True)
'''
import time
for i in range(10):
    print('{}'.format(i))
    time.sleep(1)