from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[4, 5, 1, 9], 5], Output=[4, 1, 9]))

	def get_testcases(self):
		return self.testcases
