from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=11891, Output=99009))
		self.testcases.append(case(Input=90, Output=99))

	def get_testcases(self):
		return self.testcases
