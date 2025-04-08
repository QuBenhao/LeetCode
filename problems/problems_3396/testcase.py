from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 2, 3, 4, 2, 3, 3, 5, 7], Output=2))
		self.testcases.append(case(Input=[4, 5, 6, 4, 4], Output=2))
		self.testcases.append(case(Input=[6, 7, 8, 9], Output=0))
		self.testcases.append(case(Input=[5,7,11,12,12], Output=2))

	def get_testcases(self):
		return self.testcases
