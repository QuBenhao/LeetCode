from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 2, 3, 4, 5], Output=15))
		self.testcases.append(case(Input=[1, 1, 0, 1, 1], Output=1))
		self.testcases.append(case(Input=[1, 2, -1, -2, 1, 0, -1], Output=3))

	def get_testcases(self):
		return self.testcases
