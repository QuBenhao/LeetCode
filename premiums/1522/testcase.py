from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, None, 3, 2, 4, None, 5, 6], Output=3))
		self.testcases.append(case(Input=[1, None, 2, None, 3, 4, None, 5, None, 6], Output=4))
		self.testcases.append(case(Input=[1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None, 14], Output=7))

	def get_testcases(self):
		return self.testcases
