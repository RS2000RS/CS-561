import math
total = 0
print("Problem 2 --------------- \nInput some numbers : ")
while True:
	num = int(input())
	if num % 2 == 0:
		total += num
	if num % 5 == 0:
		break
print("    "+str(total))	


