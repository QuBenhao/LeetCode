from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 4], [1, 3], [2, 4], [1, 3]], Output=[[2, 4], [1, 3], [2, 4], [1, 3]]))
		self.testcases.append(case(Input=[[]], Output=[[]]))
		self.testcases.append(case(Input=[], Output=[]))

	def get_testcases(self):
		return self.testcases
