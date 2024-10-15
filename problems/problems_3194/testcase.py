from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[7, 8, 3, 4, 15, 13, 4, 1], Output=5.5))
		self.testcases.append(case(Input=[1, 9, 8, 3, 10, 5], Output=5.5))
		self.testcases.append(case(Input=[1, 2, 3, 7, 8, 9], Output=5.0))

	def get_testcases(self):
		return self.testcases
