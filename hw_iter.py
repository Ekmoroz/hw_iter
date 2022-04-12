nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]


#1
class FlatIterator:

	def __init__(self, elements):
		self.elements = elements
		self.n = -1
		self.m = -1

	def __iter__(self):
		new = []
		for x in self.elements:
			for y in x:
				new.append(y)
		return iter(new)

	def __next__(self):
		if self.m < len(self.elements[self.n]) - 1:
			self.m += 1
			return self.elements[self.n][self.m]
		else:
			raise StopIteration


for item in FlatIterator(nested_list):
    print(item)


flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)


#2

# def flat_generator(lst):
# 	for i in lst:
# 		for y in i:
# 			yield y
#
#
# for item in flat_generator(nested_list):
# 	print(item)