import math
class C1:
	s =""
	x = 0 
	y = 0

	def __init__(self, s, x, y):
		self.s = s 
		self.x = x
		self.y = y

	def swap (self):
		z = self.x
		self.x=self.y
		self.y = z

	def add (self, other):
		return C1(self.s+"-"+other.s,self.x + other.x,self.y+other.y)
	
	def sum (self):
		return self.x + self.y

def distance(a):
	return abs(a.x - a.y)

def main():

	a = C1("hello",1,4)
	b = C1("bye",5,2)
	a.swap()
	print(a.x)
	print(b.add(a).s)
	print(a.sum())
	print(distance(b))

main()


