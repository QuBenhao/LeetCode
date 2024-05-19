from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 2, 3, None, None, 4, 5], Output=2))
		self.testcases.append(case(Input=[1, 2], Output=1))
		self.testcases.append(case(Input=[1, 2, 3, None, None, 4, None, 5, 6], Output=3))

	def get_testcases(self):
		return self.testcases
