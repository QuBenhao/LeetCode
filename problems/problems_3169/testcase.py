from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[10, [[5, 7], [1, 3], [9, 10]]], Output=2))
		self.testcases.append(case(Input=[5, [[2, 4], [1, 3]]], Output=1))
		self.testcases.append(case(Input=[6, [[1, 6]]], Output=0))
		self.testcases.append(case(Input=[8,[[3,4],[4,8],[2,5],[3,8]]], Output=1))

	def get_testcases(self):
		return self.testcases
