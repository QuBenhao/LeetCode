from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[5, 6, 1], Output=6.0))
		self.testcases.append(case(Input=[0, None, 1], Output=1.0))

	def get_testcases(self):
		return self.testcases
