from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, 5, 7, 8, 9, 2, 3, 4, 3, 1], Output=3))
		self.testcases.append(case(Input=[1, 2, 3, 4, 4, 4, 4, 5, 6, 7], Output=2))

	def get_testcases(self):
		return self.testcases
