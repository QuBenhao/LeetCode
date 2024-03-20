from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 7, 11, 15], 9], Output=[0, 1]))
		self.testcases.append(case(Input=[[3, 2, 4], 6], Output=[1, 2]))
		self.testcases.append(case(Input=[[3, 3], 6], Output=[0, 1]))

	def get_testcases(self):
		return self.testcases
