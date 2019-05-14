import math

#list, function

# Assume Without Checking: li is a list of floats
# write a func name sq with arg li that returns a 
#	parallel list, each item in the returned list 
#  is 0 (if original # is negative) or the sqrt
# 	of the original number ( if the original # is
#	non negative.  
#  for example, sq([1.0, 1.21, 0.0, -9.0])
#	return [1.0, 1.1, 0.0, 0.0]
# write a main that send a list of floats to you
# 	sq function and let maian output the returned list


def sqrtList(li): 
	result = []
	for i in li:
		if i<0:
			result.append(0.0)
		else:
			result.append(math.sqrt(i))
	return result


# Assume without checking: list of lists of ints; li has >0 elements
# 	li[0] has > 0 lements, all elements of li have the 
#	same number of elements (so li is a rectangular
#	2-dimensional list). Futher assume that the number of elements
#  in li is equal to the number of elements in li[0] (so li is a 
# 	square 2-dimensional list).
# Return whether li is a magic square: the sum of all rows, all 
#  columns, and both diagnols are all equal. 
# Name the func magicSquare;
#	pass [[2,7,6],[9,5,1],[4,3,8]] to your function & output the result.

#| !getRow(li, liSum) | !getDiag(li, liSum)

def magicSquare(li):
	liSum = getSum(li)
	if (getRow(li, liSum) == False) | (getCol(li, liSum) == False) | (getDiag(li, liSum) == False):
		return False
	return True
	
def getRow(li, liSum):
	for i in range(len(li)):
		result = 0
		for j in li[i]:
			result+= j
		if result != liSum:
			return False
	return True

def getCol(li, liSum):
	for i in range(len(li[0])):
		result = 0
		for j in range(len(li)):
			result+= li[i][j]
		if result != liSum:
			return False
	return True

def getDiag(li, liSum):
	result1 = 0
	result2 = 0
	for i in range(len(li)):
		result1 += li[i][i]
		result2 += li[len(li)-i-1][i]
	if result1 != liSum | result2 != liSum:
		return False
	return True

def getSum(li):
	result = 0
	for i in li[0]:
		result+=i
	return result


# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# QWERTYUIOPASDFGHJKLZXCVBNM
#
# I LIKE PIZZA
# O SOAT HOMMQ
#
# encode('QWERTYUIOPASDFGHJKLZXCVBNM', 'I LIKE PIZZA')
#	returns 'O SOAT HOMMQ'

def encode(key, s):
	result = ''
	alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	for c in range(len(s)):
		if s[c] == ' ':
			result+=s[c]		
		else:
			result+=key[find(s[c],alph)]
	return result
		

def find(c, s):
	for i in range(len(s)):
		if c == s[i]:
			return i
	return -1
	
# Output('data.txt', ['red', 'green', 'blue'])
#	will output each line of the file 'data.txt'
#	that contains a primary color as a substring

def output(fileName, colors):
	myFile = open(fileName, "r")
	for line in myFile:
		if findColor(line, colors):
			print(line)

def findColor(line, colors):
	index = 0
	for color in colors:
		if color in line:
			return True
	return False


def main():
	print(sqrtList([1.0, 1.21, 0.0, -9.0]))
	print(magicSquare([[2,7,6],[9,5,1],[4,3,8]]))
	print(encode('QWERTYUIOPASDFGHJKLZXCVBNM', 'I LIKE PIZZA'))
	output('data.txt', ['red', 'green', 'blue'])

main()
