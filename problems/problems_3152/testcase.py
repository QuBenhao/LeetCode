from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 4, 1, 2, 6], [[0, 4]]], Output=[False]))
		self.testcases.append(case(Input=[[4, 3, 1, 6], [[0, 2], [2, 3]]], Output=[False, True]))

	def get_testcases(self):
		return self.testcases
