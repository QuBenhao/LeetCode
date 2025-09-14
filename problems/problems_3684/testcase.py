from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[84, 93, 100, 77, 90], 3], Output=[100, 93, 90]))
		self.testcases.append(case(Input=[[84, 93, 100, 77, 93], 3], Output=[100, 93, 84]))
		self.testcases.append(case(Input=[[1, 1, 1, 2, 2, 2], 6], Output=[2, 1]))

	def get_testcases(self):
		return self.testcases
