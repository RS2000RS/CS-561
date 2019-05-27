import math

def average(lin):
	avg= 0;
	for x in lin:
		avg += int(x)
	return avg / len(lin)

def median(lin):
    lst = convert(lin)
    n = len(lst)
    if n < 1:
            return None
    if n % 2 == 1:
            return sorted(lst)[n//2]
    else:
            return sum(sorted(lst)[n//2-1:n//2+1])/2.0

def convert(lin):
  newList = []
  for x in lin:
    newList.append(int(x))    
  return newList

def remove(lin):
  lis = ""
  for x in lin:
    if x is not '\n':
      lis += x
  return lis

inFile = input('Input file name : ')
outFile = input('Output file name : ')
inF=open(inFile, "r")
outF=open(outFile, "w")
i = 1		
for lin in inF:
	outLine = str(i) + " " + remove(lin) + " " + str(average(lin.split())) + " " + str(median(lin.split())) + "\n"
	outF.write(outLine)
	i+=1
	
inF.close() 
outF.close()











