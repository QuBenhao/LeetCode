from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=23, Output="1000"))
		self.testcases.append(case(Input=107, Output="101100"))

	def get_testcases(self):
		return self.testcases
