from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[9, 12, 5, 10, 14, 3, 10], 10], Output=[9, 5, 3, 10, 10, 12, 14]))
		self.testcases.append(case(Input=[[-3, 4, 3, 2], 2], Output=[-3, 2, 4, 3]))

	def get_testcases(self):
		return self.testcases
