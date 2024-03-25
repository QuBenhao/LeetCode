from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]], Output=[[3, 4]]))
		self.testcases.append(case(Input=[[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]], Output=[[5, 6], [7, 9]]))

	def get_testcases(self):
		return self.testcases
