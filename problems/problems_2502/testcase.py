from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['Allocator', 'allocate', 'allocate', 'allocate', 'freeMemory', 'allocate', 'allocate', 'allocate', 'freeMemory', 'allocate', 'freeMemory'], [[10], [1, 1], [1, 2], [1, 3], [2], [3, 4], [1, 1], [1, 1], [1], [10, 2], [7]]], Output=[None, 0, 1, 2, 1, 3, 1, 6, 3, -1, 0]))

	def get_testcases(self):
		return self.testcases
