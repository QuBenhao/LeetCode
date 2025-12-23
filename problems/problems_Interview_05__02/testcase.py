from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=0.625, Output="0.101"))
		self.testcases.append(case(Input=0.1, Output=None))

	def get_testcases(self):
		return self.testcases
