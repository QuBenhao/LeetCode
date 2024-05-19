from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 2, 5, 3, 4, None, 6], Output=[1, None, 2, None, 3, None, 4, None, 5, None, 6]))
		self.testcases.append(case(Input=[], Output=[]))
		self.testcases.append(case(Input=[0], Output=[0]))

	def get_testcases(self):
		return self.testcases
