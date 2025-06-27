from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[20, 10, 5], Output=9))
		self.testcases.append(case(Input=[5, 10, 10], Output=1))

	def get_testcases(self):
		return self.testcases
