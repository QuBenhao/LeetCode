from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, [[1, 1, 2, 2], [0, 0, 1, 1]]], Output=[[1, 1, 0], [1, 2, 1], [0, 1, 1]]))
		self.testcases.append(case(Input=[2, [[0, 0, 1, 1]]], Output=[[1, 1], [1, 1]]))

	def get_testcases(self):
		return self.testcases
