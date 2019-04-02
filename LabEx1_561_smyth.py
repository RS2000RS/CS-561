#CS 561, Lab Ex 8, Ravela Smyth

import datetime
import math

now = datetime.datetime.now()
#
#print str(now)

#inp = input("d r: ")
#a = inp.split(' ')

#def volume(d, radius):
#	if d == 0: return 1
#	if d == 1: return 2*radius
#        return volume(d-2, radius) * math.pi * radius * radius / (d/2) 

#print("Volume is: " + volume(int(a[0]),int(a[1])))
#
def prime(num):
	if num > 1: 
      		for i in range(2, num//2):  
        		if (num % i) == 0: 
          			return False
           			break
   		else: 
       			return True
  
	else:                      "
?|      
   		return False

f = open("data.txt", "w")



def nth_prime_number(n):
    f.write(str(2) + " ") 
    if n==1: 
        return 2
    count = 1
    num = 1
    while(count < n):
        num +=2
        if prime(num):
	    if count%10 == 0:
		f.write("\n")
	    f.write(str(num) + " ")
            count +=1
    return num

print ("The 1000th prime number is " + str(nth_prime_number(1000)))

f.close()
