from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, 1, 4, 3], Output=2))
		self.testcases.append(case(Input=[2, 4, 1, 3], Output=3))
		self.testcases.append(case(Input=[1, 3, 4, 2, 5], Output=0))

	def get_testcases(self):
		return self.testcases
