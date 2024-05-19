from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[0, 2, -5, 5, 10, -10], Output=[-10, -5, 0, 2, 5, 10]))
		self.testcases.append(case(Input=[0, 1, 2], Output=[0, 1, 2]))
		self.testcases.append(case(Input=[1], Output=[1]))

	def get_testcases(self):
		return self.testcases
