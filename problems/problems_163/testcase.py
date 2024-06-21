from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[0, 1, 3, 50, 75], 0, 99], Output=[[2, 2], [4, 49], [51, 74], [76, 99]]))
		self.testcases.append(case(Input=[[-1], -1, -1], Output=[]))

	def get_testcases(self):
		return self.testcases
