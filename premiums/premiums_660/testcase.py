from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=9, Output=10))
		self.testcases.append(case(Input=10, Output=11))

	def get_testcases(self):
		return self.testcases
