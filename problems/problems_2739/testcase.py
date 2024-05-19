from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[5, 10], Output=60))
		self.testcases.append(case(Input=[1, 2], Output=10))
		self.testcases.append(case(Input=[6, 1], Output=70))

	def get_testcases(self):
		return self.testcases
