from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=31, Output=3))
		self.testcases.append(case(Input=22, Output=4))
		self.testcases.append(case(Input=124, Output=8))

	def get_testcases(self):
		return self.testcases
