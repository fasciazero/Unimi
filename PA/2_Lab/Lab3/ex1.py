from math import tan,pi,sqrt

class Polygon:
	def __init__(self,side,side_len):
		self.side = side
		self.side_len = side_len
		self.apothem = side_len / (2 * tan(pi/2/side*2))
		self.calculate_perimeter()
		self.calculate_area()
	def calculate_perimeter(self):
		self.perimeter = self.side * self.side_len
	def calculate_area(self):
		self.area = self.side * self.side_len * self.apothem / 2
	def __str__(self):
		return '{} with {} side of {} and apotehm {:.1f} - Perimeter: {:.1f} - Area {:.1f}'.format(self.name,self.side,self.side_len,self.apothem,self.perimeter,self.area)

class Triangle(Polygon):
	def __init__(self,side_len):
		self.name = 'Triangle'
		super(Triangle,self).__init__(3,side_len)

class Square(Polygon):
	def __init__(self,side_len):
		self.name = 'Square'
		super(Square,self).__init__(4,side_len)

class Pentagon(Polygon):
	def __init__(self,side_len):
		self.name = 'Pentagon'
		super(Pentagon,self).__init__(5,side_len)


class Exagon(Polygon):
	def __init__(self,side_len):
		self.name = 'Exagon'
		super(Exagon,self).__init__(6,side_len)

class Circle(Polygon):
	def __init__(self,radius):
		self.radius = radius
		self.name = 'Circle'
		self.calculate_area()
		self.calculate_perimeter()
	def calculate_area(self):
		self.area = pi * (self.radius ** 2)
	def calculate_perimeter(self):
		self.perimeter = 2 * pi * self.radius
	def __str__(self):
		return '{} with radius {} - Perimeter: {:.1f} - Area {:.1f}'.format(self.name,self.radius,self.perimeter,self.area)

class Rectangle(Polygon):
	def __init__(self,base,height):
		self.base = base
		self.height = height
		self.name = 'Rectangle'
		self.calculate_area()
		self.calculate_perimeter()
	def calculate_area(self):
		self.area = self.base * self.height
	def calculate_perimeter(self):
		self.perimeter = (self.base + self.height) * 2
	def __str__(self):
		return '{} with base {} and height {} - Perimeter: {:.1f} - Area {:.1f}'.format(self.name,self.base,self.height,self.perimeter,self.area)

if __name__ == '__main__':
	figures = sorted([Triangle(7),Square(7),Pentagon(7),Exagon(7),Circle(7),Rectangle(6,7)],key=lambda x:x.area)
	for f in figures: print(f)