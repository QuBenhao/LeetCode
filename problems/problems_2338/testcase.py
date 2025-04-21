from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, 5], Output=10))
		self.testcases.append(case(Input=[5, 3], Output=11))

	def get_testcases(self):
		return self.testcases
