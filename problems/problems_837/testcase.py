from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[10, 1, 10], Output=1.0))
		self.testcases.append(case(Input=[6, 1, 10], Output=0.6))
		self.testcases.append(case(Input=[21, 17, 10], Output=0.73278))

	def get_testcases(self):
		return self.testcases
