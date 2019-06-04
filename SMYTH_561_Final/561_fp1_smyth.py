import math

r = input("Input side of a regular hexagon: ")
if r < 0:
	print("Negative?!")
else:	
	print("Area is = " + str(r * r * math.sqrt(3) * 3 / 2) + "\n")
