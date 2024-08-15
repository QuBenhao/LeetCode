from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[-1, 0, 1, 2, -1, -4], Output=[[-1, -1, 2], [-1, 0, 1]]))
		self.testcases.append(case(Input=[], Output=[]))
		self.testcases.append(case(Input=[0], Output=[]))

	def get_testcases(self):
		return self.testcases
