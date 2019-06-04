import math

li = []
sumLi = 0

while True:
	num = input()
	if num != 0:
		li.append(num)
		sumLi += num
	else:
		break

def getMedian(li):
  theValues = sorted(li)
  if len(theValues) % 2 == 1:
    return theValues[(len(theValues)+1)/2-1]
  else:
    lower = theValues[len(theValues)/2-1]
    upper = theValues[len(theValues)/2]
    return (float(lower + upper)) / 2 


def getRange(li):
	minLi = li[0]
	maxLi = li[0]
	for x in li:
		if x < minLi:
			minLi = x
		if x > maxLi:
			maxLi = x
	return [minLi, maxLi]

def stdev(li):
	return math.sqrt(variance(li))

def variance(li):
	v = 0
	for x in li:
		v += (x-(sumLi/len(li)))**2
	return (float(v))/len(li)


print( "Average : ", sumLi / len(li))
print( "Range : " , getRange(li))
print( "Median : ", getMedian(li))
print( "Standard Deviation : ", stdev(li))

