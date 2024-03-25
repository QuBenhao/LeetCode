from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, 3, 3, 3, 3], Output=1))
		self.testcases.append(case(Input=[1, 1, 1, 3, 9, 9, 9, 2, 10, 10], Output=5))
		self.testcases.append(case(Input=[1, 2, 3, 4, 5, 6, 7], Output=7))

	def get_testcases(self):
		return self.testcases
