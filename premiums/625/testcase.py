from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=48, Output=68))
		self.testcases.append(case(Input=15, Output=35))

	def get_testcases(self):
		return self.testcases
