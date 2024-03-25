from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[5, 1, 5, 5, 5, None, 5], Output=4))
		self.testcases.append(case(Input=[], Output=0))
		self.testcases.append(case(Input=[5, 5, 5, 5, 5, None, 5], Output=6))

	def get_testcases(self):
		return self.testcases
