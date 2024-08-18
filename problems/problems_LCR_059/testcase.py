from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['KthLargest', 'add', 'add', 'add', 'add', 'add'], [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]], Output=[None, 4, 5, 5, 8, 8]))

	def get_testcases(self):
		return self.testcases
