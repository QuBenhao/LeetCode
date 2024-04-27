from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=2, Output="110"))
		self.testcases.append(case(Input=3, Output="111"))
		self.testcases.append(case(Input=4, Output="100"))

	def get_testcases(self):
		return self.testcases
