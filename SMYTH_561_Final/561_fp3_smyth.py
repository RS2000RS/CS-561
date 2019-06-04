import math

def f1(n):
    if isinstance(n, int) & (n>0):	
        count = 0
        for i in range(2, int(pow(n, 1 / 2))+1): 
            if n % i == 0: 
                count+=1
        return count		
    else:
        print("I don't know what this input is!")


print(f1(96))



def f2(li):
	if (all(isinstance(x, int) for x in li) & all(x>0 for x in li)):	
		result = 0
		for i in li:
			result = gcd(result, i)
		return result
	else:
			print("I don't know what this input is!")

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a



def f3(n):
	if isinstance(n, int) & (n>=0):	
		if n == 0:
			return 0
		elif n == 1:
			return 1
		else:
			return(f3(n-1) + f3(n-2))
	else:
		print("I don't know what this input is!")



def f4(li):
	if all(isinstance(x, list) for x in li):	
		resultLi = []
		for x in li:
			for y in x:
				resultLi.append(y)
		return resultLi
	else:
		print("I don't know what this input is!")


print(f2([8,12]))
print(f3(10))
print(f4([[1,2,3],[3,2,1],[],[1,2,3]]))


