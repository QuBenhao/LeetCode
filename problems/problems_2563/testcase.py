from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[0, 1, 7, 4, 4, 5], 3, 6], Output=6))
		self.testcases.append(case(Input=[[1, 7, 9, 2, 5], 11, 11], Output=1))

	def get_testcases(self):
		return self.testcases
