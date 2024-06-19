from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, 5, 1, 4], Output=5))
		self.testcases.append(case(Input=[11, 21, 12], Output=2))

	def get_testcases(self):
		return self.testcases
