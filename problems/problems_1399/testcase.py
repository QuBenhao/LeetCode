from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=13, Output=4))
		self.testcases.append(case(Input=2, Output=2))

	def get_testcases(self):
		return self.testcases
