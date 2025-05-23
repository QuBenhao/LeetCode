from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 2, 3, None, 5, None, 4], Output=[1, 3, 4]))
		self.testcases.append(case(Input=[1, None, 3], Output=[1, 3]))
		self.testcases.append(case(Input=[], Output=[]))
		self.testcases.append(case(Input=[1,2,3,4], Output=[1,3,4]))

	def get_testcases(self):
		return self.testcases
