from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 2, 3, 4], Output=10))
		self.testcases.append(case(Input=[6, 5, 7, 8], Output=7))
		self.testcases.append(case(Input=[8, 7, 6, 6], Output=3))

	def get_testcases(self):
		return self.testcases
