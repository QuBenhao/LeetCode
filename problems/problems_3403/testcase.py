from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['dbca', 2], Output="dbc"))
		self.testcases.append(case(Input=['gggg', 4], Output="g"))
		self.testcases.append(case(Input=["aann",2], Output="nn"))

	def get_testcases(self):
		return self.testcases
