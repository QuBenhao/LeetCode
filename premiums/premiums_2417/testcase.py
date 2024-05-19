from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=2, Output=10))
		self.testcases.append(case(Input=403, Output=1001))

	def get_testcases(self):
		return self.testcases
