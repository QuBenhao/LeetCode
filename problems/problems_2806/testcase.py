from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=9, Output=90))
		self.testcases.append(case(Input=15, Output=80))

	def get_testcases(self):
		return self.testcases
