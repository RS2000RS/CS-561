import math

def f(x):
	if isinstance(x, float) and (x >= 0) :
		return math.sqrt(x) * 3
	
def without(s0,s1):
	if isinstance(s0, str) and isinstance(s1, str):
		result = ""
		for x in s0:
			if x not in s1:
				result += x
		return result

def f1(li):
	if (isfloats(li)):
		newLi = []
		for x in li:
			if x >= 1:
				newLi.insert(0, f(x))
		return newLi
		
def f2(li):
	if li and isListFloats(li):
		newList = []
		for x in li:
			newList.append(getMaxMin(x))
		return newList
		
		
def isListFloats(li):
	for y in li:
		for x in y:
			if isinstance(x, float) is False and ( x != 0):
					return False
	return True

def getMaxMin(li):
	maxMin = [li[0], li[0]]
	for x in li:
		if x > maxMin[1]:
			maxMin[1] = x
		if x < maxMin[0]:
			maxMin[0] = x
	return maxMin

def isfloats(li):
	for x in li:
		if isinstance(x, float) is False and ( x != 0):
			return False
	return True


 
print ("Problem 3 --------------- \n")
print ("f(4.234) : " + str(f(4.234)))
print ("f(-1) : " + str(f(-1)))
print ("without('abracadabra, 'Yabba Dabba') : '" + without('abracadabra', 'Yabba Dabba'))
print ("'f1([0.5, -47.0, 9.0, 0, 4.0, 16.0]) : ", f1([0.5, -47.0, 9.0, 0, 4.0, 16.0]))
print ("f2([[1.0,2.0,3.0],[5.0],[10.0,9.0,8.0,7.0]]) :" , f2([[1.0,2.0,3.0],[5.0],[10.0,9.0,8.0,7.0]])) 	


