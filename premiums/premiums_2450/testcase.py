from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['1001', 3], Output=4))
		self.testcases.append(case(Input=['10110', 5], Output=2))

	def get_testcases(self):
		return self.testcases
