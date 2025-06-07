from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=13, Output=[1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]))
		self.testcases.append(case(Input=2, Output=[1, 2]))

	def get_testcases(self):
		return self.testcases
