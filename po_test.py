class Point:

	def __init__(self,x=0,y=0):

		self.x = x
		self.y = y

	def distance_from_origiin(self):

		return ((self.x ** 2) + (self.y ** 2)) ** 0.5

	def __str__(self):

		return "({0},{1})".format(self.x,self.y)

	def midpoint(p1,p2):

		mx = (p1.x + p2.x)/2
		my = (p1.y + p2.y)/2
		return Point(mx,my)

	def halfway(self,target):

		mx = (self.x + target.x)/2
		my = (self.y + target.y)/2
		return Point(mx,my)

	def reflect(self):

		return Point(self.x,0-self.y)

	def slope_from_origin(self):

		return self.y/self.x
		#当x坐标为0时会失败

	def get_line_to(self,target):
		a = (self.y - target.y)/(self.x - target.x)
		b = self.y - self.x * a
		return Point(a,b)
		#当点点的x坐标相同时会失败

p = Point(4,10)
#q = Point(5,12)
#print(Point(3,4).halfway(Point(5,12)))
#r = Point.midpoint(p,q)
#print(p.distance_from_origiin())
#print(str(p))
#print(r)
print(p.reflect())
print(p.slope_from_origin())

print(Point(4,11).get_line_to(Point(6,15)))