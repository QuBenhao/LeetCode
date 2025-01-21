from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, 4, 1, 2, 7, 8], Output=9))
		self.testcases.append(case(Input=[2, 4, 5], Output=4))
		self.testcases.append(case(Input=[9, 8, 7, 6, 5, 1, 2, 3, 4], Output=18))

	def get_testcases(self):
		return self.testcases
