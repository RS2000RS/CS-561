inFile = input('Input file name : ')
outFile = input('Output file name : ')
inF=open(inFile, "r")
outF=open(outFile, "w")

def getAvg(li):
    avg = 0.0
    for x in li:
        avg += x
    return avg/len(li)

for lin in inF:
    li = [float(x) for x in lin.split()]
    outLine = str(getAvg(li)) + ": " + lin
    outF.write(outLine)
	
inF.close() 
outF.close()



