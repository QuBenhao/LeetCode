from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=22, Output=2))
		self.testcases.append(case(Input=8, Output=0))
		self.testcases.append(case(Input=5, Output=2))

	def get_testcases(self):
		return self.testcases
