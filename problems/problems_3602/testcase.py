from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=13, Output="A91P1"))
		self.testcases.append(case(Input=36, Output="5101000"))

	def get_testcases(self):
		return self.testcases
