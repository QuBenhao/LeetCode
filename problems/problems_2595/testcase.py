from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=50, Output=[1, 2]))
		self.testcases.append(case(Input=2, Output=[0, 1]))
		self.testcases.append(case(Input=5, Output=[2,0]))

	def get_testcases(self):
		return self.testcases
