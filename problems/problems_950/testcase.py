from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[17, 13, 11, 2, 3, 5, 7], Output=[2, 13, 3, 11, 5, 17, 7]))
		self.testcases.append(case(Input=[1, 1000], Output=[1, 1000]))

	def get_testcases(self):
		return self.testcases
