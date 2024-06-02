from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[7, 4], Output=[1, 2, 3, 1]))
		self.testcases.append(case(Input=[10, 3], Output=[5, 2, 3]))
		self.testcases.append(case(Input=[90, 4], Output=[27, 18, 21, 24]))

	def get_testcases(self):
		return self.testcases
