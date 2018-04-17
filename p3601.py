class Rectangle:
	length = 5
	width =4
	
	def setRect(self):
		print('Input length and width:')
		self.length = float(raw_input('Length: ')
		self.width = float(raw_input('Width: '))
		
	def getRect(self):
		print('Rectangle length is: $.2f, width is %.2f' %(self.length, self.width))
		
	def getArea(self):
		return self.length * self.width