from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, 10, 7, 5, 4, 1, 8, 6], Output=5))
		self.testcases.append(case(Input=[0, -4, 19, 1, 8, -2, -3, 5], Output=3))
		self.testcases.append(case(Input=[101], Output=1))

	def get_testcases(self):
		return self.testcases
