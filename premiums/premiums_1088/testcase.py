from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=20, Output=6))
		self.testcases.append(case(Input=100, Output=19))

	def get_testcases(self):
		return self.testcases
