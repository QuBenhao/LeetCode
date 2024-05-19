from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 3, 5, 4, 4, 6], Output=10))
		self.testcases.append(case(Input=[1, 2, 3, 4, 5], Output=15))

	def get_testcases(self):
		return self.testcases
