from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="(()())", Output=[0, 1, 1, 1, 1, 0]))
		self.testcases.append(case(Input="()(())()", Output=[0, 0, 0, 1, 1, 0, 1, 1]))

	def get_testcases(self):
		return self.testcases
