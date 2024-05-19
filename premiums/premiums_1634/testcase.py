from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[1, 1]], [[1, 0]]], Output=[[1, 1], [1, 0]]))
		self.testcases.append(case(Input=[[[2, 2], [4, 1], [3, 0]], [[3, 2], [-4, 1], [-1, 0]]], Output=[[5, 2], [2, 0]]))
		self.testcases.append(case(Input=[[[1, 2]], [[-1, 2]]], Output=[]))

	def get_testcases(self):
		return self.testcases
