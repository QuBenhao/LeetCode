from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[-10, -3, 0, 5, 9], Output=[0, -3, 9, -10, None, 5]))
		self.testcases.append(case(Input=[1, 3], Output=[3, 1]))

	def get_testcases(self):
		return self.testcases
