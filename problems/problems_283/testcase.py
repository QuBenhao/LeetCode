from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[0, 1, 0, 3, 12], Output=[1, 3, 12, 0, 0]))
		self.testcases.append(case(Input=[0], Output=[0]))

	def get_testcases(self):
		return self.testcases
