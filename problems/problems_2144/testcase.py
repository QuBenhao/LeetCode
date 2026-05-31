from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 2, 3], Output=5))
		self.testcases.append(case(Input=[6, 5, 7, 9, 2, 2], Output=23))
		self.testcases.append(case(Input=[5, 5], Output=10))
		self.testcases.append(case(Input=[3,3,3,1], Output=7))

	def get_testcases(self):
		return self.testcases
