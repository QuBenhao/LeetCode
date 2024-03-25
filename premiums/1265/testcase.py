from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 2, 3, 4], Output=[4, 3, 2, 1]))
		self.testcases.append(case(Input=[0, -4, -1, 3, -5], Output=[-5, 3, -1, -4, 0]))
		self.testcases.append(case(Input=[-2, 0, 6, 4, 4, -6], Output=[-6, 4, 4, 6, 0, -2]))

	def get_testcases(self):
		return self.testcases
