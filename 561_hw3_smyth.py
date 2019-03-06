#  561_hw3_smyth.py
#  Smyth, Ravela
#  CS561 HW3 "Standard Deviation"  

import math

f = open('input')
data = []
mean = 0
for line in f:
	for num in line.split(' '):
 		data.append(int(num))
		mean += int(num)
		print(num)
f.close()


mean /= len(data)
stddev = 0

for num in data:
	stddev += (num - mean) * (num - mean)
stddev = math.sqrt(stddev / len(data))

print("Your standard deviation is " , stddev)

