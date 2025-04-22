from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, 1, 3], Output=1))
		self.testcases.append(case(Input=[1, 2, 3, 4, None, 5, 6, None, None, 7], Output=7))

	def get_testcases(self):
		return self.testcases
