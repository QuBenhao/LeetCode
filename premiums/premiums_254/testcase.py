from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=1, Output=[]))
		self.testcases.append(case(Input=12, Output=[[2, 6], [3, 4], [2, 2, 3]]))
		self.testcases.append(case(Input=37, Output=[]))

	def get_testcases(self):
		return self.testcases
