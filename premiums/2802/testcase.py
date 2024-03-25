from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=4, Output="47"))
		self.testcases.append(case(Input=10, Output="477"))
		self.testcases.append(case(Input=1000, Output="777747447"))

	def get_testcases(self):
		return self.testcases
