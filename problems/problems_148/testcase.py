from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[4, 2, 1, 3], Output=[1, 2, 3, 4]))
		self.testcases.append(case(Input=[-1, 5, 3, 4, 0], Output=[-1, 0, 3, 4, 5]))
		self.testcases.append(case(Input=[], Output=[]))

	def get_testcases(self):
		return self.testcases
