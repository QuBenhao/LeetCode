from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[5, 4, 5, 1, 1, None, 5], Output=2))
		self.testcases.append(case(Input=[1, 4, 5, 4, 4, None, 5], Output=2))

	def get_testcases(self):
		return self.testcases
