import random
import math

def new(fileName, N):
    f=open(fileName, 'w')
    for i in range(N):
        f.write(str(random.gauss(0,1))+'\n')
    f.close()

def readFile (fileName):
    floats=[]
    f=open(fileName, 'r')
    for x in f:
        floats.append(float(x))
    f.close()
    return floats
    
    
def percentage(li, num):
    count = 0
    for n in li:
        if n>=num:
            count += 1 
    return count / len(li)
    

new('data.dat', 1000000)
li=[]
li=readFile('data.dat')
print('% of number >=1 SD above mean','{0:8.4f}'.format(percentage(li,1)))
print('% of number >=2 SD above mean','{0:8.4f}'.format(percentage(li,2)))
print('% of number >=3 SD above mean','{0:8.4f}'.format(percentage(li,3)))
