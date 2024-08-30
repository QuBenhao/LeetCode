from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 2, 3, 4], Output=[24, 12, 8, 6]))
		self.testcases.append(case(Input=[-1, 1, 0, -3, 3], Output=[0, 0, 9, 0, 0]))

	def get_testcases(self):
		return self.testcases
