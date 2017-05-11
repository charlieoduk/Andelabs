class BinarySearch(list):
	"""docstring for BinarySearch"""
	def __init__(self, a, b):
		super().__init__()
		self.length = a
		self.b = b

		for i in range(self.length):
			list.append(self,self.b)
			self.b += b


	def search(self, num):
		def binary(self, list, num):
			midpoint = len(list)//2
			count = 0
			if list[midpoint] == num:
				return {'count':count,'index':midpoint}
			else:
				if num < list[midpoint]:
					count += 1
					return binary(list[:midpoint], num)
				else:
					count += 1
					return binary(list[midpoint+1:], num)
		