from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[0, 3, 1, 0, 4, 5, 2, 0], Output=[4, 11]))
		self.testcases.append(case(Input=[0, 1, 0, 3, 0, 2, 2, 0], Output=[1, 3, 4]))

	def get_testcases(self):
		return self.testcases
