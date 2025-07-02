from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=5, Output="b"))
		self.testcases.append(case(Input=10, Output="c"))
		self.testcases.append(case(Input=4, Output="c"))

	def get_testcases(self):
		return self.testcases
