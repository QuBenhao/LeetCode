from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, 9, 20, None, None, 15, 7], Output=[[3], [20, 9], [15, 7]]))
		self.testcases.append(case(Input=[1], Output=[[1]]))
		self.testcases.append(case(Input=[], Output=[]))

	def get_testcases(self):
		return self.testcases
