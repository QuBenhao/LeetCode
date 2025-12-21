from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=25, Output=27))
		self.testcases.append(case(Input=10, Output=9))
		self.testcases.append(case(Input=7, Output=0))

	def get_testcases(self):
		return self.testcases
